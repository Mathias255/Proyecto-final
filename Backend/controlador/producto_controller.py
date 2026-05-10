from flask import jsonify, request
from modelo.productos import Producto
from database import db

def listar_productos():
    productos = Producto.query.all()
    return jsonify([p.to_dict() for p in productos]), 200

def obtener_producto(id):
    p = Producto.query.get(id)
    return jsonify(p.to_dict()) if p else (jsonify({"error": "No existe"}), 404)

def guardar_producto():
    data = request.json
    nuevo = Producto(nombre=data['nombre'], precio=data['precio'], stock=data['stock'], categoria_id=data.get('categoria_id'))
    db.session.add(nuevo)
    db.session.commit()
    return jsonify({"msj": "Producto creado"}), 201

def actualizar_producto(id):
    p = Producto.query.get(id)
    if not p: return jsonify({"msj": "No encontrado"}), 404
    data = request.json
    p.nombre, p.precio, p.stock = data.get('nombre', p.nombre), data.get('precio', p.precio), data.get('stock', p.stock)
    db.session.commit()
    return jsonify({"msj": "Actualizado"}), 200

def eliminar_producto(id):
    p = Producto.query.get(id)
    if not p: return jsonify({"msj": "No encontrado"}), 404
    db.session.delete(p)
    db.session.commit()
    return jsonify({"msj": "Eliminado"}), 200