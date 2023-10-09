import datetime

class Pedidos():

    def __init__(self):
        self.__fecha_factura = datetime.date.today()
        self.__valor_total_pedido = 0
        self.__producto_control = [] 
        self.__antibiotico = []
    
    @property
    def fecha_factura(self):
        return self.__fecha_factura

    @fecha_factura.setter
    def fecha_factura(self, fecha_factura):
        self.__fecha_factura = fecha_factura

    @property
    def valor_total_pedido(self):
        return self.__valor_total_pedido

    @valor_total_pedido.setter
    def valor_total_pedido(self, valor_total_pedido):
        self.__valor_total_pedido += valor_total_pedido
        
    @property
    def producto_control(self):
        return self.__producto_control

    @producto_control.setter
    def producto_control(self, producto_control):
        self.__producto_control.append(producto_control)

    def asociar_producto_control(self, producto_control):
        self.producto_control.append(producto_control)
        self.valor_total_pedido = producto_control.valor_producto

    @property
    def antibiotico(self):
        return self.__antibiotico
    
    @antibiotico.setter
    def antibiotico(self, antibiotico):
        self.__antibiotico.append(antibiotico)

    def asociar_antibiotico(self,antibiotico):
        self.antibiotico.append(antibiotico)
        self.valor_total_pedido = antibiotico.valor_producto
