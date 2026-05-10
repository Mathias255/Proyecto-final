from flask import Blueprint
from controlador.producto_controller import *

productos_bp = Blueprint('productos_bp', __name__)

productos_bp.route('/', methods=['GET'])(listar_productos)
productos_bp.route('/<int:id>', methods=['GET'])(obtener_producto)
productos_bp.route('/', methods=['POST'])(guardar_producto)
productos_bp.route('/<int:id>', methods=['PUT'])(actualizar_producto)
productos_bp.route('/<int:id>', methods=['DELETE'])(eliminar_producto)