from flask import Flask, request, jsonify

app = Flask(__name__)

@app.post("/api/alerts")
def receive_alert():
    alert = request.get_json()
    print("Alert received:", alert)
    return jsonify({"status": "received"}), 200

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)