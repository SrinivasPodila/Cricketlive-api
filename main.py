from flask import Flask, jsonify
from scraper import get_live_scores  # <-- Import here
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome! Use /live-scores to get live cricket scores."

@app.route("/live-scores")
def live_scores():
    data = get_live_scores()
    if isinstance(data, dict) and "error" in data:
        return jsonify(data), 500
    return jsonify(data)

@app.route("/api/matches")
def api_matches():
    data = get_live_scores()
    if isinstance(data, dict) and "error" in data:
        return jsonify(data), 500
    return jsonify(data)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
