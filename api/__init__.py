""" API for time series predictions for the Superstore dataset. """

import json
import os

import flask
import prophet.serialize

THIS_FOLDER = os.path.dirname(__file__)
ROOT_FOLDER = os.path.join(*os.path.split(THIS_FOLDER)[:-1])
MODEL_PATH = os.path.join(ROOT_FOLDER, "model", "model.json")

app = flask.Flask(__name__)

with open(MODEL_PATH) as file:
    model = prophet.serialize.model_from_json(json.load(file))


def _forecast_sales(periods):
    """Forecast sales."""
    future = model.make_future_dataframe(periods=periods, include_history=False)
    forecast = model.predict(future)
    forecast = forecast.set_index("ds")
    forecast = forecast["yhat"]
    forecast.index = forecast.index.astype(str)
    return forecast.to_dict()


@app.route("/v1/sales/")
def orders():
    """Get sales forecast."""
    periods = flask.request.args.get("days")
    return _forecast_sales(int(periods))
