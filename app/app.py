from flask import Flask, request, jsonify
from datetime import datetime
import logging

app = Flask(__name__)

# Simple in-memory mock database
items_db = {
    1: {"name": "Laptop", "price": 55000},
    2: {"name": "Mouse", "price": 600},
    3: {"name": "Keyboard", "price": 1200}
}

APP_VERSION = "2.0.1"

# -------------------------------------------------------
# Logging Configuration
# -------------------------------------------------------
logging.basicConfig(filename="app.log",
                    level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

@app.before_request
def log_request():
    logging.info(f"{request.method} request at {request.path}")

# -------------------------------------------------------
# ROUTES
# -------------------------------------------------------

@app.route("/")
def home():
    return """
    <h1>🚀 DevOps Flask Demo</h1>
    <p>This is a fully automated CI/CD Flask application.</p>
    <h3>Available Endpoints:</h3>
    <ul>
        <li>GET /items → Fetch all items</li>
        <li>GET /items/&lt;id&gt; → Fetch a single item</li>
        <li>POST /items → Add new item</li>
        <li>PUT /items/&lt;id&gt; → Update item</li>
        <li>DELETE /items/&lt;id&gt; → Delete item</li>
        <li>GET /health → Health check</li>
        <li>GET /version → App version</li>
    </ul>
    """

# -------------------------------------------------------
# API ENDPOINTS (CRUD)
# -------------------------------------------------------

@app.route("/items", methods=["GET"])
def get_items():
    return jsonify({"items": items_db})

@app.route("/items/<int:item_id>", methods=["GET"])
def get_item(item_id):
    item = items_db.get(item_id)
    if item:
        return jsonify({"item": item})
    return jsonify({"error": "Item not found"}), 404

@app.route("/items", methods=["POST"])
def add_item():
    data = request.json
    new_id = max(items_db.keys()) + 1
    items_db[new_id] = data
    return jsonify({"message": "Item added successfully", "id": new_id})

@app.route("/items/<int:item_id>", methods=["PUT"])
def update_item(item_id):
    if item_id not in items_db:
        return jsonify({"error": "Item not found"}), 404

    data = request.json
    items_db[item_id].update(data)
    return jsonify({"message": "Item updated", "item": items_db[item_id]})

@app.route("/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    if item_id not in items_db:
        return jsonify({"error": "Item not found"}), 404

    del items_db[item_id]
    return jsonify({"message": "Item deleted"})

# -------------------------------------------------------
# HEALTH CHECK
# -------------------------------------------------------

@app.route("/health")
def health():
    return jsonify({"status": "UP", "timestamp": datetime.now().isoformat()})

# -------------------------------------------------------
# VERSION
# -------------------------------------------------------

@app.route("/version")
def version():
    return jsonify({"version": APP_VERSION})

# -------------------------------------------------------

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
