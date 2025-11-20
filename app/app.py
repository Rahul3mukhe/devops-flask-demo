from flask import Flask, jsonify, request, render_template, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__, static_folder="static", template_folder="templates")

# config
DB_PATH = os.environ.get("DATABASE_URL", "sqlite:///data.db")
app.config["SQLALCHEMY_DATABASE_URI"] = DB_PATH
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# simple versioning
APP_VERSION = os.environ.get("APP_VERSION", "v1.0.0")

# Model
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140), nullable=False)
    description = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description or "",
            "created_at": self.created_at.isoformat()
        }

# create DB if does not exist
with app.app_context():
    db.create_all()

# Routes
@app.route("/")
def index():
    return render_template("index.html")

# API endpoints
@app.route("/health")
def health():
    return jsonify({"status": "ok"}), 200

@app.route("/version")
def version():
    return jsonify({"version": APP_VERSION}), 200

@app.route("/items", methods=["GET"])
def get_items():
    q = request.args.get("q", "")
    if q:
        items = Item.query.filter(Item.name.ilike(f"%{q}%")).order_by(Item.id.desc()).all()
    else:
        items = Item.query.order_by(Item.id.desc()).all()
    return jsonify([i.to_dict() for i in items])

@app.route("/items/<int:item_id>", methods=["GET"])
def get_item(item_id):
    item = Item.query.get_or_404(item_id)
    return jsonify(item.to_dict())

@app.route("/items", methods=["POST"])
def create_item():
    data = request.get_json() or {}
    name = data.get("name")
    description = data.get("description", "")
    if not name:
        return jsonify({"error": "name is required"}), 400
    item = Item(name=name, description=description)
    db.session.add(item)
    db.session.commit()
    return jsonify(item.to_dict()), 201

@app.route("/items/<int:item_id>", methods=["PUT"])
def update_item(item_id):
    item = Item.query.get_or_404(item_id)
    data = request.get_json() or {}
    item.name = data.get("name", item.name)
    item.description = data.get("description", item.description)
    db.session.commit()
    return jsonify(item.to_dict())

@app.route("/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    item = Item.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    return jsonify({"deleted": True})

# Serve static files if needed
@app.route("/static/<path:filename>")
def static_files(filename):
    return send_from_directory(app.static_folder, filename)

if __name__ == "__main__":
    # run dev server (not for production)
    app.run(host="0.0.0.0", port=5000, debug=True)
