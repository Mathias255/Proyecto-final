from database import db

class Categoria(db.Model):
    __tablename__ = 'categorias'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), unique=True, nullable=False)
    descripcion = db.Column(db.String(200))
    # Relación con productos
    productos = db.relationship('Producto', backref='categoria_rel', lazy=True)

    def to_dict(self):
        return {"id": self.id, "nombre": self.nombre, "descripcion": self.descripcion}