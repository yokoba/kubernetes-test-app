import os

from flask import Flask

app = Flask(__name__)


@app.route("/")
def root():
    return "Hello World!"


@app.route("/pod", methods=["GET"])
def get_pod_name():
    name = os.environ.get("POD_NAME")
    return name


if __name__ == "__main__":
    HOST = os.environ.get("FLASK_HOST", "localhost")
    PORT = int(os.environ.get("FLASK_PORT", 5000))

    app.run(port=PORT, host=HOST)
