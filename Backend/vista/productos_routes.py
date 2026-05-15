from flask import Blueprint
from controlador.producto_controller import (
    listar_productos, obtener_producto, crear_producto, 
    actualizar_producto, parchear_producto, eliminar_producto
)

productos_bp = Blueprint('productos_bp', __name__)

# Prefijo en app.py: /api/productos
productos_bp.route('/', methods=['GET'])(listar_productos)
productos_bp.route('/<int:id>', methods=['GET'])(obtener_producto) # BUSCAR POR ID
productos_bp.route('/', methods=['POST'])(crear_producto)
productos_bp.route('/<int:id>', methods=['PUT'])(actualizar_producto)
productos_bp.route('/<int:id>', methods=['PATCH'])(parchear_producto)
productos_bp.route('/<int:id>', methods=['DELETE'])(eliminar_producto)