from flask import Flask, jsonify, request
from data import products

app = Flask(__name__)

products = [
    {"id": 1, "name": "Laptop", "category": "electronics"},
    {"id": 2, "name": "Book", "category": "books"},
    {"id": 3, "name": "Notebook", "category": "books"},
]

# TODO: Implement homepage route that returns a welcome message
@app.route("/")
def home():
    return jsonify({"message":"Welcome to the Gulag"}) # TODO: Return a welcome message



# TODO: Implement GET /products route that returns all products or filters by category
@app.route("/products")
def get_products():
    category = request.args.get("category")
    if category:
        filtered = [p for p in products if p["category"].lower() == category.lower()]
        return jsonify(filtered)
    return jsonify(products)


# TODO: Implement GET /products/<id> route that returns a specific product by ID or 404
@app.route("/products/<int:id>")
def get_product_by_id(id):
    product = None  # TODO: Find product by ID
    for p in products:
        if p["id"] == id:
            product = p
            break
        
    
    if product:
        return jsonify(product)
    else:
        return jsonify({"error": "Product not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
