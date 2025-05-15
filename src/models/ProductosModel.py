from database.db import get_connection
from .entities.Productos import Productos

class ProductosModel():
    
    @classmethod
    def get_productos(self):
        try:
            connection=get_connection()
            productos=[]
            
            
            with connection.cursor() as cursor:
                cursor.execute("SELECT id_producto,categoria_producto,id_compra,caracteristicas_producto,tipo_producto,tamano_producto,precio_producto,mes_del_producto,nombre_producto FROM productos ORDER BY nombre_producto ASC") 
                resultset=cursor.fetchall()
                
                for row in resultset:
                    producto=Productos(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8])
                    productos.append(producto.to_JSON())
                    
            connection.close()
            return productos        
                
        except Exception as ex:
            return Exception(ex)    
        
    @classmethod
    def get_producto(self,id_producto):
        try:
            connection=get_connection()
            
            with connection.cursor() as cursor:
                cursor.execute("SELECT id_producto,categoria_producto,id_compra,caracteristicas_producto,tipo_producto,tamano_producto,precio_producto,mes_del_producto,nombre_producto FROM productos WHERE id_producto = %s",(id_producto,)) 
                row=cursor.fetchone()
                
                producto=None
                if row != None:
                    producto=Productos(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8])
                    producto=producto.to_JSON()
                    
            connection.close()
            return producto       
                
        except Exception as ex:
            return Exception(ex)        
        