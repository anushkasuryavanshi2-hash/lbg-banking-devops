from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "service": "Customer Service",
        "status": "running"
    })


@app.route("/customers")
def customers():
    return jsonify({
        "customers": [
            {
                "id": 1,
                "name": "John Doe"
            },
            {
                "id": 2,
                "name": "Jane Smith"
            }
        ]
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)