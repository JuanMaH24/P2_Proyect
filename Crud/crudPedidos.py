import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from Modelo.Pedidos import Pedidos
class CrudPedidos():

    def __init__(self):
        self.facturas_creadas = []

    def create_factura(self, clientes = None, cedula_cliente = None):
        nueva_factura = Pedidos()
        self.facturas_creadas.append(nueva_factura)
        clientes.update_factura_cliente(cedula_cliente, nueva_factura)
        mensaje = "Factura creada exitosamente"
        return {"Mensaje": mensaje, "Factura": nueva_factura}

    def read(self):
        facturas = self.facturas_creadas
        return facturas
    
    def buscar_factura(self, clientes = None, cedula_cliente = None):
        cliente = clientes.buscar_cedula(cedula_cliente)
        for factura in self.facturas_creadas:
            if factura in cliente.factura:
                mensaje = "Factura encontrada"
                return {"Mensaje": mensaje, "Factura": factura}
        mensaje = "No se encontró la f"
        return {"Mensaje": mensaje, "Cliente": None}


    

