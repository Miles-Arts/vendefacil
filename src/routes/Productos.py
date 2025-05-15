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
    
    return jsonify({'message': "Vende_Productos"})

