from flask import Flask
from flask_cors import CORS
from database import db

# 1. IMPORTACIÓN DE BLUEPRINTS
from vista.productos_routes import productos_bp
from vista.categorias_routes import categorias_bp
from vista.usuarios_routes import usuarios_bp
from vista.orden_routes import orden_bp

app = Flask(__name__)

# --- AJUSTE CRÍTICO DE CORS ---
# Permitimos explícitamente el origen de Angular (localhost:4200) 
# y los métodos necesarios para tu CRUD.
CORS(app, resources={r"/api/*": {"origins": "*"}}, supports_credentials=True)

# 2. CONFIGURACIÓN DE LA BASE DE DATOS
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@localhost:5432/tienda_computadoras'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 3. INICIALIZACIÓN
db.init_app(app)

# 4. REGISTRO DE RUTAS
app.register_blueprint(productos_bp, url_prefix='/api/productos')
app.register_blueprint(categorias_bp, url_prefix='/api/categorias')
app.register_blueprint(usuarios_bp, url_prefix='/api/usuarios')
app.register_blueprint(orden_bp, url_prefix='/api/ordenes')

@app.route('/')
def index():
    return {
        "status": "online",
        "mensaje": "Nanobot Systems Backend Operacional",
        "version": "1.1"
    }

# 5. CREACIÓN DE TABLAS
with app.app_context():
    try:
        import modelo.categoria
        import modelo.productos
        import modelo.usuarios
        import modelo.orden
        
        db.create_all()
        print("---------------------------------------")
        print(" NANOBOT DATABASE: ONLINE ")
        print("---------------------------------------")
    except Exception as e:
        print(f"Error en DB: {e}")

if __name__ == '__main__':
    # Usamos host='0.0.0.0' para asegurar que sea visible en la red local
    app.run(debug=True, port=5000, host='0.0.0.0')