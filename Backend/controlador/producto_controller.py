from flask import jsonify, request
from database import db
from modelo.productos import Producto

def listar_productos():
    items = Producto.query.all()
    return jsonify([i.to_dict() for i in items])

def guardar_producto():
    data = request.json
    nuevo = Producto(
        nombre=data['nombre'], 
        precio=data['precio'], 
        stock=data['stock'], 
        categoria_id=data.get('categoria_id')
    )
    db.session.add(nuevo)
    db.session.commit()
    return jsonify({"msj": "Creado"}), 201