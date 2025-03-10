from flask import Flask, request, jsonify
from database import db

app = Flask(__name__)
collection = db["clientes"]

@app.route("/clientes", methods=["POST"])
def crear_cliente():
    data = request.json
    if not data.get("nombre") or not data.get("email"):
        return jsonify({"error": "Nombre y email son obligatorios"}), 400

    collection.insert_one(data)
    return jsonify({"mensaje": "Cliente creado con éxito"}), 201

@app.route("/clientes/<email>", methods=["GET"])
def obtener_cliente(email):
    cliente = collection.find_one({"email": email}, {"_id": 0})
    if not cliente:
        return jsonify({"error": "Cliente no encontrado"}), 404
    return jsonify(cliente), 200

if __name__ == "__main__":
    app.run(debug=True)

