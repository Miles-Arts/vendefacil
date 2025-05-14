class Productos():
    
    def __init__(self,id_producto,categoria_producto=None,id_compra=None,caracteristicas_producto=None,tipo_producto=None,tamaño_producto=None,precio_producto=None,mes_del_producto=None,nombre_producto=None) -> None:
        self.id_producto=id_producto
        self.categoria_producto=categoria_producto
        self.id_compra=id_compra
        self.caracteristicas_producto=caracteristicas_producto
        self.tipo_producto=tipo_producto
        self.tamaño_producto=tamaño_producto
        self.precio_producto=precio_producto
        self.mes_del_producto=mes_del_producto
        self.nombre_producto=nombre_producto
        
        
    def to_JSON(self):
        return { 
            'id_producto':self.id_producto,
            'categoria_producto':self.categoria_producto,
            'id_compra':self.id_compra,
            'caracteristicas_producto':self.caracteristicas_producto,
            'tipo_producto':self.tipo_producto,
            'tamaño_producto':self.tamaño_producto,
            'precio_producto':self.precio_producto,
            'mes_del_producto':self.mes_del_producto,
            'nombre_producto':self.nombre_producto
        }   