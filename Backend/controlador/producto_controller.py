from flask import jsonify, request
from modelo.productos import Producto
from database import db

def listar_productos():
    productos = Producto.query.all()
    return jsonify([p.to_dict() for p in productos]), 200

def obtener_producto(id):
    p = Producto.query.get(id)
    return jsonify(p.to_dict()) if p else (jsonify({"error": "Producto no encontrado"}), 404)

def crear_producto(): 
    data = request.json
    nuevo = Producto(
        nombre=data['nombre'], 
        precio=data['precio'], 
        stock=data['stock'], 
        categoria_id=data.get('categoria_id')
    )
    db.session.add(nuevo)
    db.session.commit()
    return jsonify({"msj": "Producto creado", "id": nuevo.id}), 201

def actualizar_producto(id):
    p = Producto.query.get(id)
    if not p: return jsonify({"error": "No encontrado"}), 404
    data = request.json
    p.nombre = data['nombre']
    p.precio = data['precio']
    p.stock = data['stock']
    p.categoria_id = data.get('categoria_id')
    db.session.commit()
    return jsonify({"msj": "Producto actualizado"}), 200

def parchear_producto(id):
    p = Producto.query.get(id)
    if not p: return jsonify({"error": "No encontrado"}), 404
    data = request.json
    if 'nombre' in data: p.nombre = data['nombre']
    if 'precio' in data: p.precio = data['precio']
    if 'stock' in data: p.stock = data['stock']
    if 'categoria_id' in data: p.categoria_id = data['categoria_id']
    db.session.commit()
    return jsonify({"msj": "Campo actualizado"}), 200

def eliminar_producto(id):
    p = Producto.query.get(id)
    if not p: return jsonify({"error": "No encontrado"}), 404
    db.session.delete(p)
    db.session.commit()
    return jsonify({"msj": "Eliminado"}), 200