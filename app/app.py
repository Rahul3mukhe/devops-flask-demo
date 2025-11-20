from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>DevOps Flask Demo</title>
        <style>
            body { font-family: Arial; padding: 20px; }
            h1 { color: #2c3e50; }
            ul { font-size: 18px; }
            li { margin: 6px 0; }
        </style>
    </head>

    <body>
        <h1>🚀 DevOps Flask Demo</h1>
        <p>This is a fully automated CI/CD Flask application deployed using Jenkins.</p>

        <h3>Available Endpoints:</h3>
        <ul>
            <li>GET /items → Fetch all items</li>
            <li>GET /items/&lt;id&gt; → Fetch one item</li>
            <li>POST /items → Add new item</li>
            <li>PUT /items/&lt;id&gt; → Update item</li>
            <li>DELETE /items/&lt;id&gt; → Delete item</li>
            <li>GET /health → Health check</li>
            <li>GET /version → App version</li>
        </ul>
    </body>
    </html>
    """

# sample items
items = [
    {"id": 1, "name": "Laptop"},
    {"id": 2, "name": "Mouse"}
]

@app.route("/items", methods=["GET"])
def get_items():
    return jsonify(items)

@app.route("/items/<int:item_id>", methods=["GET"])
def get_item(item_id):
    for item in items:
        if item["id"] == item_id:
            return jsonify(item)
    return jsonify({"error": "Item not found"}), 404

@app.route("/items", methods=["POST"])
def add_item():
    data = request.json
    new_item = {"id": len(items) + 1, "name": data["name"]}
    items.append(new_item)
    return jsonify(new_item), 201

@app.route("/items/<int:item_id>", methods=["PUT"])
def update_item(item_id):
    data = request.json
    for item in items:
        if item["id"] == item_id:
            item["name"] = data["name"]
            return jsonify(item)
    return jsonify({"error": "Item not found"}), 404

@app.route("/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    global items
    items = [item for item in items if item["id"] != item_id]
    return jsonify({"message": "Item deleted"})

@app.route("/health")
def health():
    return jsonify({"status": "OK"})

@app.route("/version")
def version():
    return jsonify({"version": "2.0.0"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
