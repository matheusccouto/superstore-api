""" API for time series predictions for the Superstore dataset. """

import json
import os
from typing import Dict

import flask
import prophet.serialize

THIS_FOLDER = os.path.dirname(__file__)
ROOT_FOLDER = os.path.join(*os.path.split(THIS_FOLDER)[:-1])
MODEL_PATH = os.path.join(ROOT_FOLDER, "model", "model.json")

app = flask.Flask(__name__)

with open(MODEL_PATH) as file:
    model = prophet.serialize.model_from_json(json.load(file))
    app.logger.info("Machine learning model loading was succesful.")


def _forecast_sales(periods: int) -> Dict[str, float]:
    """Forecast sales."""
    future = model.make_future_dataframe(
        periods=periods,
        freq="W",
        include_history=False,
    )
    forecast = model.predict(future)
    forecast = forecast.set_index("ds")
    forecast = forecast["yhat"]
    forecast.index = forecast.index.astype(str)
    return forecast.to_dict()


@app.route("/")
def home() -> str:
    """Home page."""
    return "<h1>Superstore API</h1>Time series predictions for the Superstore dataset"


@app.route("/v1/sales/")
def orders() -> Dict[str, float]:
    """Get sales forecast."""
    periods = int(flask.request.args.get("weeks"))
    return _forecast_sales(periods=periods)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
