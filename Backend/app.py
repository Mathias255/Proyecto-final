from flask import Flask
from flask_cors import CORS
from database import db

# 1. Importación de tus Rutas (Blueprints)
from vista.productos_routes import productos_bp
from vista.categorias_routes import categorias_bp
from vista.usuarios_routes import usuarios_bp
from vista.orden_routes import orden_bp

app = Flask(__name__)
CORS(app)

# 2. Configuración de PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@localhost:5432/tienda_computadoras'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 3. Inicialización de la base de datos
db.init_app(app)

# 4. Registro de los Blueprints (API)
app.register_blueprint(productos_bp, url_prefix='/api/productos')
app.register_blueprint(categorias_bp, url_prefix='/api/categorias')
app.register_blueprint(usuarios_bp, url_prefix='/api/usuarios')
app.register_blueprint(orden_bp, url_prefix='/api/ordenes')

# --- RUTA DE BIENVENIDA (Para evitar el 404 al inicio) ---
@app.route('/')
def home():
    return {
        "status": "online",
        "mensaje": "Servidor de Tienda de Computadoras Funcionando 🚀",
        "endpoints": [
            "/api/productos",
            "/api/categorias",
            "/api/usuarios"
        ]
    }
# --------------------------------------------------------

# 5. Creación de tablas
with app.app_context():
    db.create_all()
    print("Tablas verificadas/creadas exitosamente.")

if __name__ == '__main__':
    app.run(debug=True, port=5000)