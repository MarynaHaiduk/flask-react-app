import os

from dotenv import load_dotenv
from flask import Flask, jsonify
from flask_cors import CORS
from data import products

load_dotenv()

app = Flask(__name__)
CORS(app)

HOST = os.getenv("FLASK_HOST", "127.0.0.1")
PORT = int(os.getenv("FLASK_PORT", "5000"))
DEBUG = os.getenv("FLASK_DEBUG", "false").lower() == "true"

@app.route("/")
def home():
    return "Flask API is running!"

@app.route("/api/products", methods=["GET"])
def get_products():
    return jsonify(products)

@app.route("/api/products/<int:product_id>", methods=["GET"])
def get_product(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
    if product is None:
        return jsonify({"error": "Product not found"}), 404
    return jsonify(product)

@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({
        "status": "OK",
        "environment": os.getenv("FLASK_ENV", "development")
    })

if __name__ == "__main__":
    app.run(host=HOST, port=PORT, debug=DEBUG)
