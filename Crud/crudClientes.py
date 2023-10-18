import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from Modelo.Clientes import Clientes

class ClientesCrud():
    def __init__(self):
        self.clientes = []
    
    def create(self, nombre = None, cedula_cliente = None):
        nuevo_cliente = Clientes(nombre, cedula_cliente)
        self.clientes.append(nuevo_cliente)
        mensaje = "Cliente creado exitosamente"
        return {"Mensaje": mensaje, "Cliente": nuevo_cliente}

    def read(self):
        clientes = self.clientes 
        return clientes
    
    def buscar_cedula(self,cedula_cliente=None):
        for cliente in self.clientes:
            if cedula_cliente == cliente.cedula:
                mensaje = "Cliente encontrado"
                return {"Mensaje": mensaje, "Cliente": cliente}
            else:
                mensaje= "No se encontró al cliente"
                return {"Mensaje": mensaje, "Cliente": None}
    
    #Agregar facturas a un cliente ya creado
    def update_factura_cliente(self, cedula_cliente = None,factura = None):
        cliente = self.buscar_cedula(cedula_cliente)
        if cliente != None:
            cliente["Cliente"].asociar_factura(factura)
            mensaje= "Se actualizó correctamente las facturas del cliente"
            return {"Mensaje": mensaje, "Cliente": None}
        else:
            mensaje= "No se encontró al cliente"
            return {"Mensaje": mensaje, "Cliente": None}

#

    












