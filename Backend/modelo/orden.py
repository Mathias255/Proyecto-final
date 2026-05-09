from database import db
from datetime import datetime

class Orden(db.Model):
    __tablename__ = 'ordenes'
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.DateTime, default=datetime.utcnow)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    total = db.Column(db.Float, nullable=False)
    
    # Detalles de la orden (productos comprados)
    detalles = db.relationship('DetalleOrden', backref='orden', lazy=True)

class DetalleOrden(db.Model):
    __tablename__ = 'detalles_orden'
    id = db.Column(db.Integer, primary_key=True)
    orden_id = db.Column(db.Integer, db.ForeignKey('ordenes.id'), nullable=False)
    producto_id = db.Column(db.Integer, db.ForeignKey('productos.id'), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    precio_unitario = db.Column(db.Float, nullable=False)