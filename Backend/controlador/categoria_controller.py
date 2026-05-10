from flask import jsonify, request
from modelo.categoria import Categoria
from database import db

def listar_categorias():
    return jsonify([c.to_dict() for c in Categoria.query.all()]), 200

# CAMBIA EL NOMBRE AQUÍ: de guardar_categoria a crear_categoria
def crear_categoria():
    data = request.json
    nueva = Categoria(nombre=data['nombre'], descripcion=data.get('descripcion'))
    db.session.add(nueva)
    db.session.commit()
    return jsonify({"msj": "Categoría creada"}), 201

def eliminar_categoria(id):
    c = Categoria.query.get(id)
    if not c: return jsonify({"msj": "No existe"}), 404
    db.session.delete(c)
    db.session.commit()
    return jsonify({"msj": "Categoría eliminada"}), 200