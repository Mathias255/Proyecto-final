from flask import Flask
from flask_cors import CORS
from database import db

# 1. IMPORTACIÓN DE TODOS LOS BLUEPRINTS
# Asegúrate de que los nombres coincidan con los de tus archivos en /vista
from vista.productos_routes import productos_bp
from vista.categorias_routes import categorias_bp
from vista.usuarios_routes import usuarios_bp
from vista.orden_routes import orden_bp

app = Flask(__name__)

# Configuración de CORS: Fundamental para que Angular (puerto 4200) 
# pueda hablar con Flask (puerto 5000)
CORS(app)

# 2. CONFIGURACIÓN DE LA BASE DE DATOS
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@localhost:5432/tienda_computadoras'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 3. INICIALIZACIÓN DE SQLALCHEMY
db.init_app(app)

# 4. REGISTRO DE RUTAS
# El url_prefix define cómo empezará la URL en el navegador
app.register_blueprint(productos_bp, url_prefix='/api/productos')
app.register_blueprint(categorias_bp, url_prefix='/api/categorias')
app.register_blueprint(usuarios_bp, url_prefix='/api/usuarios')
app.register_blueprint(orden_bp, url_prefix='/api/ordenes')

# Ruta de prueba para verificar que el servidor corre
@app.route('/')
def index():
    return {
        "status": "online",
        "mensaje": "Backend de Tienda de Computo listo",
        "version": "1.0"
    }

# 5. CREACIÓN DE TABLAS (Solo si no existen)
with app.app_context():
    try:
        # Importamos los modelos aquí para que SQLAlchemy los reconozca al crear las tablas
        import modelo.categoria
        import modelo.productos
        import modelo.usuarios
        import modelo.orden
        
        db.create_all()
        print("---------------------------------------")
        print(" ESTRUCTURA DE BASE DE DATOS LISTA ")
        print("---------------------------------------")
    except Exception as e:
        print(f"Error al conectar/crear tablas: {e}")

if __name__ == '__main__':
    # El debug=True es clave mientras programas para que se reinicie solo
    app.run(debug=True, port=5000)