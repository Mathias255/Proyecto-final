from flask import Blueprint
# Aquí importamos los nombres que acabamos de definir
from controlador.usuario_controller import listar_usuarios, crear_usuario, obtener_usuario

usuarios_bp = Blueprint('usuarios_bp', __name__)

usuarios_bp.route('/', methods=['GET'])(listar_usuarios)
usuarios_bp.route('/<int:id>', methods=['GET'])(obtener_usuario)
usuarios_bp.route('/', methods=['POST'])(crear_usuario)