from flask import Blueprint
from controlador.categoria_controller import (
    listar_categorias, obtener_categoria_id, crear_categoria, 
    parchear_categoria, eliminar_categoria
)

categorias_bp = Blueprint('categorias_bp', __name__)

# Prefijo en app.py: /api/categorias
categorias_bp.route('/', methods=['GET'])(listar_categorias)
categorias_bp.route('/<int:id>', methods=['GET'])(obtener_categoria_id) # BUSCAR POR ID
categorias_bp.route('/', methods=['POST'])(crear_categoria)
categorias_bp.route('/<int:id>', methods=['PATCH'])(parchear_categoria)
categorias_bp.route('/<int:id>', methods=['DELETE'])(eliminar_categoria)