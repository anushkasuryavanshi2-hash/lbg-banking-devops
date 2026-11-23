from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "service": "Notification Service",
        "status": "running"
    })


@app.route("/notifications")
def notifications():
    return jsonify({
        "notifications": [
            {
                "notification_id": "NOT001",
                "customer_id": 1,
                "message": "Your payment of 5000 was successful",
                "status": "Sent"
            },
            {
                "notification_id": "NOT002",
                "customer_id": 2,
                "message": "Your account statement is ready",
                "status": "Pending"
            }
        ]
    })


@app.route("/notifications/<notification_id>")
def notification(notification_id):
    return jsonify({
        "notification_id": notification_id,
        "status": "Sent"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)