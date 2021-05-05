import flask

app = flask.Flask(__name__)


@app.route("/")
def home():
    """ Home page. """
    return "<h1>Superstore API</h1>Time series predictions for the Superstore dataset"


@app.route("/v1/orders/")
def orders():
    """ Get inbound orders prediction """
    return flask.jsonify({
            "foo": "bar"
        })
