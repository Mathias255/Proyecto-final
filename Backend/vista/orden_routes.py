from flask import Blueprint
from controlador.orden_controller import (
    listar_ordenes, obtener_orden, crear_orden, eliminar_orden
)

orden_bp = Blueprint('orden_bp', __name__)

# Prefijo en app.py: /api/ordenes
orden_bp.route('/', methods=['GET'])(listar_ordenes)
orden_bp.route('/<int:id>', methods=['GET'])(obtener_orden) # BUSCAR POR ID
orden_bp.route('/', methods=['POST'])(crear_orden)
orden_bp.route('/<int:id>', methods=['DELETE'])(eliminar_orden)