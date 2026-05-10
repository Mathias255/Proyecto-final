from flask import Blueprint
from controlador.categoria_controller import listar_categorias, crear_categoria

categorias_bp = Blueprint('categorias_bp', __name__)

@categorias_bp.route('/', methods=['GET'])
def get_categorias():
    return listar_categorias()

@categorias_bp.route('/', methods=['POST'])
def post_categoria():
    return crear_categoria()