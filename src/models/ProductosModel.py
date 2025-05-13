from database.db import get_connection
from .entities.Productos import Productos

class ProductosModel():
    
    def get_productos(self):
        try:
            connection=get_connection()
            productos=[]
            
            
            with connection.cursor() as cursor:
                cursor.execute("SELECT id_producto,categoria_producto,id_compra,caracteristicas_producto,tipo_producto,tamaño_producto,precio_producto,mes_del_producto,nombre_producto FROM productos ORDER BY nombre_producto ASC") 
                resultset=cursor.fetchall()
        except Exception as ex:
            return Exception(ex)    
        