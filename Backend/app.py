from flask import Flask
from flask_cors import CORS
from database import db

# Importar Blueprints
from vista.productos_routes import productos_bp
# (Importa los demás Blueprints de forma similar...)

app = Flask(__name__)
CORS(app)

# CONEXIÓN A POSTGRESQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@localhost:5432/tienda_computadoras'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Registro de Rutas
app.register_blueprint(productos_bp, url_prefix='/api/productos')

with app.app_context():
    db.create_all() # Esto crea las tablas en Postgres automáticamente
    print("Tablas creadas exitosamente.")

if __name__ == '__main__':
    app.run(debug=True)