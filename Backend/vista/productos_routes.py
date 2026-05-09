from flask import Blueprint
from controlador.producto_controller import listar_productos, guardar_producto

productos_bp = Blueprint('productos_bp', __name__)

productos_bp.route('/', methods=['GET'])(listar_productos)
productos_bp.route('/', methods=['POST'])(guardar_producto)