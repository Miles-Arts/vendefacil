from flask import Blueprint
from flask import jsonify
from flask import request
import uuid

#Entities
from models.entities.Productos import Productos

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
    
@main.route('/add',methods=['POST'])    
def add_producto():
    
    try:
        #Validar datos correcto y que no sean entregados vacios o erroneos en el campo requerido
        #id_producto=request.json['id_producto']
        categoria_producto=request.json['categoria_producto']
        id_compra=int(request.json['id_compra'])
        caracteristicas_producto=request.json['caracteristicas_producto']
        tipo_producto=request.json['tipo_producto']
        tamano_producto=int(request.json['tamano_producto'])
        precio_producto=float(request.json['precio_producto'])
        mes_del_producto=request.json['mes_del_producto']
        nombre_producto=request.json['nombre_producto']
        
        id=uuid.uuid4()
        #print(id)
        producto=Productos(str(id),categoria_producto,id_compra,caracteristicas_producto,tipo_producto,tamano_producto,precio_producto,mes_del_producto,nombre_producto)
        
        affected_rows=  ProductosModel.add_producto(producto)
        
        if affected_rows == 1:
            return jsonify(producto.id_producto)
        else:
            return jsonify({'massage': "Error al agregar Producto"}), 500 
        
    except Exception as ex:
        return jsonify({'massage': str(ex)}), 500     
