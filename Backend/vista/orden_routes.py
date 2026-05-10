from flask import Blueprint
from controlador.orden_controller import crear_orden

orden_bp = Blueprint('orden_bp', __name__)

@orden_bp.route('/', methods=['POST'])
def post_orden():
    return crear_orden()