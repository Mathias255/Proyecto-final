from flask import jsonify, request
from database import db
from modelo.orden import Orden, DetalleOrden
from modelo.productos import Producto

def listar_ordenes():
    return jsonify([o.to_dict() for o in Orden.query.all()]), 200

def crear_orden():
    data = request.json
    try:
        nueva_orden = Orden(usuario_id=data['usuario_id'], total=data['total'])
        db.session.add(nueva_orden)
        
        for item in data['productos']:
            p = Producto.query.get(item['id'])
            if p.stock < item['cantidad']:
                return jsonify({"error": f"Sin stock de {p.nombre}"}), 400
            
            p.stock -= item['cantidad'] # Descontamos del inventario
            detalle = DetalleOrden(orden=nueva_orden, producto_id=item['id'], 
                                  cantidad=item['cantidad'], precio_unitario=item['precio'])
            db.session.add(detalle)
        
        db.session.commit()
        return jsonify({"msj": "Compra realizada exitosamente"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500