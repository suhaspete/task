# from flask import Flask, request, jsonify

# app = Flask(__name__)

# # This is a placeholder for the actual products
# products = [
#     {
#         "id": 1,
#         "name": "Scientific Calculator",
#         "price": 499.00
#     },
#     {
#         "id": 2,
#         "name": "Lab Pant",
#         "price": 210.00
#     },
#     {
#         "id": 3,
#         "name": "Vistara T shirt",
#         "price": 299.00
#     }
# ]

# @app.route("/products")
# def get_products():
#     return jsonify(products)

# @app.route("/products/<int:product_id>")
# def get_product(product_id):
#     product = next((p for p in products if p["id"] == product_id), None)
#     if product:
#         return jsonify(product)
#     else:
#         return "Product not found", 404

# @app.route("/add-to-cart", methods=["POST"])
# def add_to_cart():
#     data = request.get_json()
#     product_id = data.get("productId")
#     quantity = data.get("quantity")
#     # Here you would add the product to the cart in the database
#     return "Product added to cart", 200

# if __name__ == "__main__":
#     app.run(debug=True)