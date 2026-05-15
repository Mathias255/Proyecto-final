from flask import jsonify, request
from modelo.usuarios import Usuario
from database import db

def listar_usuarios():
    usuarios = Usuario.query.all()
    return jsonify([u.to_dict() for u in usuarios]), 200

def obtener_usuario(id):
    u = Usuario.query.get(id)
    return jsonify(u.to_dict()) if u else (jsonify({"error": "Usuario no encontrado"}), 404)

def crear_usuario():
    data = request.json
    # Validación para evitar KeyError
    if not data or 'password' not in data:
        return jsonify({"error": "El campo 'password' es obligatorio"}), 400
    
    try:
        nuevo = Usuario(
            nombre=data.get('nombre'),
            email=data.get('email'),
            password=data['password']
        )
        db.session.add(nuevo)
        db.session.commit()
        return jsonify({"msj": "Usuario registrado", "id": nuevo.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

def actualizar_usuario(id):
    u = Usuario.query.get(id)
    if not u: return jsonify({"error": "No existe"}), 404
    data = request.json
    u.nombre = data.get('nombre', u.nombre)
    u.email = data.get('email', u.email)
    u.password = data.get('password', u.password)
    db.session.commit()
    return jsonify({"msj": "Usuario actualizado (PUT)"}), 200

def parchear_usuario(id):
    u = Usuario.query.get(id)
    if not u: return jsonify({"error": "No existe"}), 404
    data = request.json
    if 'nombre' in data: u.nombre = data['nombre']
    if 'email' in data: u.email = data['email']
    if 'password' in data: u.password = data['password']
    db.session.commit()
    return jsonify({"msj": "Usuario modificado (PATCH)"}), 200

def eliminar_usuario(id):
    u = Usuario.query.get(id)
    if not u: return jsonify({"error": "No existe"}), 404
    db.session.delete(u)
    db.session.commit()
    return jsonify({"msj": "Usuario eliminado"}), 200