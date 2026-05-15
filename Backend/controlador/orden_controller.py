from flask import jsonify, request
from database import db
from modelo.orden import Orden, DetalleOrden
from modelo.productos import Producto

def listar_ordenes():
    ordenes = Orden.query.all()
    return jsonify([o.to_dict() for o in ordenes]), 200

def obtener_orden(id):
    o = Orden.query.get(id)
    return jsonify(o.to_dict()) if o else (jsonify({"error": "Orden no encontrada"}), 404)

def crear_orden():
    data = request.json
    try:
        nueva_orden = Orden(usuario_id=data['usuario_id'], total=data['total'])
        db.session.add(nueva_orden)
        
        for item in data['productos']:
            p = Producto.query.get(item['id'])
            if not p or p.stock < item['cantidad']:
                db.session.rollback()
                return jsonify({"error": f"Stock insuficiente para {p.nombre if p else 'ID '+str(item['id'])}"}), 400
            
            p.stock -= item['cantidad']
            detalle = DetalleOrden(
                orden_perteneciente=nueva_orden,
                producto_id=item['id'],
                cantidad=item['cantidad'],
                precio_unitario=item['precio']
            )
            db.session.add(detalle)
        
        db.session.commit()
        return jsonify({"msj": "Venta exitosa", "orden_id": nueva_orden.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

def eliminar_orden(id):
    o = Orden.query.get(id)
    if not o: return jsonify({"error": "No encontrada"}), 404
    db.session.delete(o)
    db.session.commit()
    return jsonify({"msj": "Orden eliminada"}), 200