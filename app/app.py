from flask import Flask, jsonify, request, render_template_string
import logging
import datetime

app = Flask(__name__)

# -------------------------------
# Logging Setup
# -------------------------------
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# -------------------------------
# Home Page (HTML)
# -------------------------------
HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>DevOps Flask App</title>
</head>
<body style="font-family:Arial; padding:40px;">
    <h2>🚀 DevOps Flask Demo</h2>
    <p>This app is deployed automatically using Jenkins CI/CD pipeline.</p>
    <hr>
    <h3>Available Endpoints:</h3>
    <ul>
        <li>GET <b>/</b> → Home Page</li>
        <li>GET <b>/api/data</b> → Fetch sample JSON data</li>
        <li>POST <b>/api/add</b> → Add numbers</li>
        <li>GET <b>/health</b> → Health check</li>
        <li>GET <b>/version</b> → Application version</li>
    </ul>
</body>
</html>
"""

@app.route("/")
def home():
    logging.info("Home page accessed")
    return render_template_string(HTML_PAGE)

# -------------------------------
# API Endpoint: GET
# -------------------------------
@app.route("/api/data", methods=["GET"])
def get_data():
    sample = {
        "message": "Welcome to DevOps Flask API",
        "status": "success",
        "timestamp": str(datetime.datetime.now())
    }
    logging.info("Data API accessed")
    return jsonify(sample)

# -------------------------------
# API Endpoint: POST
# -------------------------------
@app.route("/api/add", methods=["POST"])
def add_numbers():
    data = request.get_json()
    
    if not data or "a" not in data or "b" not in data:
        return jsonify({"error": "Missing inputs"}), 400

    result = data["a"] + data["b"]
    logging.info(f"Add API requested: {data['a']} + {data['b']} = {result}")
    return jsonify({"result": result})

# -------------------------------
# Health Check (for Jenkins/Docker)
# -------------------------------
@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "UP"}), 200

# -------------------------------
# Version (updates every build)
# -------------------------------
@app.route("/version", methods=["GET"])
def version():
    return jsonify({
        "app": "DevOps Flask Demo",
        "version": "1.0.0",
        "deployed_at": str(datetime.datetime.now())
    })

# -------------------------------
# Run App
# -------------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
