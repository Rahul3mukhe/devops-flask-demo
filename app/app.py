from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def hello():
    name = os.environ.get("APP_NAME", "DevOpsDemo")
    version = os.environ.get("APP_VERSION", "v1.0")
    return jsonify({
        "message": f"Hello from {name}!",
        "version": version
    })

if __name__ == "__main__":
    # host 0.0.0.0 to allow outside connections from container
    app.run(host="0.0.0.0", port=5000)
