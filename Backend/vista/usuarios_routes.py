from flask import Blueprint
from controlador.usuario_controller import (
    listar_usuarios, obtener_usuario, crear_usuario, 
    actualizar_usuario, parchear_usuario, eliminar_usuario
)

usuarios_bp = Blueprint('usuarios_bp', __name__)

# Definición de todas las rutas para /api/usuarios/
usuarios_bp.route('/', methods=['GET'])(listar_usuarios)
usuarios_bp.route('/<int:id>', methods=['GET'])(obtener_usuario)
usuarios_bp.route('/', methods=['POST'])(crear_usuario)
usuarios_bp.route('/<int:id>', methods=['PUT'])(actualizar_usuario)
usuarios_bp.route('/<int:id>', methods=['PATCH'])(parchear_usuario)
usuarios_bp.route('/<int:id>', methods=['DELETE'])(eliminar_usuario)