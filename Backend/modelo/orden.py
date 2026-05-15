from database import db
from datetime import datetime

class Orden(db.Model):
    __tablename__ = 'ordenes'
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.DateTime, default=datetime.utcnow)
    total = db.Column(db.Float, nullable=False)
    
    # CLAVE FORÁNEA: Quién compró
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    
    # RELACIÓN: Una orden tiene muchos detalles
    detalles = db.relationship('DetalleOrden', backref='orden_perteneciente', lazy=True)

    def to_dict(self):
        return {
            "id": self.id,
            "fecha": self.fecha.strftime("%Y-%m-%d %H:%M:%S"),
            "usuario": self.cliente.nombre,
            "total": self.total,
            "productos": [d.to_dict() for d in self.detalles]
        }

class DetalleOrden(db.Model):
    __tablename__ = 'detalles_orden'
    id = db.Column(db.Integer, primary_key=True)
    cantidad = db.Column(db.Integer, nullable=False)
    precio_unitario = db.Column(db.Float, nullable=False)
    
    # CLAVES FORÁNEAS: A qué orden pertenece y qué producto es
    orden_id = db.Column(db.Integer, db.ForeignKey('ordenes.id'), nullable=False)
    producto_id = db.Column(db.Integer, db.ForeignKey('productos.id'), nullable=False)
    
    # Relación para obtener el nombre del producto fácilmente
    producto = db.relationship('Producto')

    def to_dict(self):
        return {
            "producto": self.producto.nombre,
            "cantidad": self.cantidad,
            "subtotal": self.cantidad * self.precio_unitario
        }