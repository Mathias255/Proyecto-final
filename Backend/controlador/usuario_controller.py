from flask import jsonify, request
from modelo.usuarios import Usuario
from database import db

def listar_usuarios():
    usuarios = Usuario.query.all()
    return jsonify([u.to_dict() for u in usuarios]), 200

# CAMBIA EL NOMBRE AQUÍ: de guardar_usuario a crear_usuario
def crear_usuario():
    data = request.json
    if not data:
        return jsonify({"error": "No se enviaron datos"}), 400
        
    nuevo_usuario = Usuario(
        nombre=data['nombre'],
        email=data['email'],
        password=data['password']
    )
    db.session.add(nuevo_usuario)
    db.session.commit()
    return jsonify({"mensaje": "Usuario creado", "id": nuevo_usuario.id}), 201

# Agrega esta si te falta para el GET por ID
def obtener_usuario(id):
    u = Usuario.query.get(id)
    return jsonify(u.to_dict()) if u else (jsonify({"msj": "No encontrado"}), 404)