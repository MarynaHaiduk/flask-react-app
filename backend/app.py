from flask import Flask, jsonify
from flask_cors import CORS
from data import products

app = Flask(__name__)
CORS(app)

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
    return jsonify({"status": "OK"})

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
