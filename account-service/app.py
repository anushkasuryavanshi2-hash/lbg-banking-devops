from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "service": "Account Service",
        "status": "running"
    })


@app.route("/accounts")
def accounts():
    return jsonify({
        "accounts": [
            {
                "account_id": "ACC001",
                "customer_id": 1,
                "account_type": "Savings",
                "balance": 50000
            },
            {
                "account_id": "ACC002",
                "customer_id": 2,
                "account_type": "Current",
                "balance": 75000
            }
        ]
    })


@app.route("/accounts/<account_id>")
def account(account_id):
    return jsonify({
        "account_id": account_id,
        "status": "Active"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)