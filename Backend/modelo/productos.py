from database import db

class Producto(db.Model):
    __tablename__ = 'productos'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, default=0)
    
    # CLAVE FORÁNEA: Conecta con la tabla categorías
    categoria_id = db.Column(db.Integer, db.ForeignKey('categorias.id'), nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "precio": self.precio,
            "stock": self.stock,
            "categoria": self.categoria_asociada.nombre if self.categoria_asociada else "Sin categoría"
        }