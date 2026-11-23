from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "service": "Payment Service",
        "status": "running"
    })


@app.route("/payments")
def payments():
    return jsonify({
        "payments": [
            {
                "payment_id": "PAY001",
                "customer_id": 1,
                "amount": 5000,
                "status": "Successful"
            },
            {
                "payment_id": "PAY002",
                "customer_id": 2,
                "amount": 2500,
                "status": "Pending"
            }
        ]
    })


@app.route("/payments/<payment_id>")
def payment(payment_id):
    return jsonify({
        "payment_id": payment_id,
        "status": "Successful"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)