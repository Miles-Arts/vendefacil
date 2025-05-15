from flask import Blueprint
from flask import jsonify

#productos
from models.ProductosModel import ProductosModel



main=Blueprint('productos_blueprint',__name__)

@main.route('/')
def get_productos():
    
    try:
        productos=ProductosModel.get_productos()
        return jsonify(productos)
        
    except Exception as ex:
        return jsonify({'massage': str(ex)}), 500 

@main.route('/<id_producto>')    
def get_producto(id_producto):
    
    try:
       producto=ProductosModel.get_producto(id_producto)
       
       if producto != None:
           return jsonify(producto)
       else:
           return jsonify({}), 404
        
    except Exception as ex:
        return jsonify({'massage': str(ex)}), 500 
