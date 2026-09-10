from flask import Flask, jsonify, request
from pathlib import Path

app = Flask(__name__)

MODEL_VERSION = "model-7"


def get_application_version():
    return (Path(__file__).resolve().parent / "VERSION").read_text().strip()


@app.route("/")
def home():
    return jsonify({
        "service": "mlops-demo",
        "status": "running"
    })


@app.route("/health")
def health():
    return jsonify({
        "application_version": get_application_version(),
        "model_version": MODEL_VERSION,
        "status": "healthy"
    })


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    value = float(data["value"])

    prediction = value * 2

    return jsonify({
        "input": value,
        "prediction": prediction,
        "application_version": get_application_version(),
        "model_version": MODEL_VERSION
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)