from flask import jsonify, request
from modelo.categoria import Categoria
from database import db

def listar_categorias():
    return jsonify([c.to_dict() for c in Categoria.query.all()]), 200

# NUEVA: Buscar categoría por ID
def obtener_categoria_id(id):
    c = Categoria.query.get(id)
    return jsonify(c.to_dict()) if c else (jsonify({"error": "Categoría no encontrada"}), 404)

def crear_categoria():
    data = request.json
    nueva = Categoria(nombre=data['nombre'], descripcion=data.get('descripcion'))
    db.session.add(nueva)
    db.session.commit()
    return jsonify({"msj": "Categoría creada"}), 201

def parchear_categoria(id):
    c = Categoria.query.get(id)
    if not c: return jsonify({"error": "No encontrado"}), 404
    data = request.json
    if 'nombre' in data: c.nombre = data['nombre']
    if 'descripcion' in data: c.descripcion = data['descripcion']
    db.session.commit()
    return jsonify({"msj": "Categoría actualizada"}), 200

def eliminar_categoria(id):
    c = Categoria.query.get(id)
    if not c: return jsonify({"error": "No encontrada"}), 404
    db.session.delete(c)
    db.session.commit()
    return jsonify({"msj": "Categoría eliminada"}), 200