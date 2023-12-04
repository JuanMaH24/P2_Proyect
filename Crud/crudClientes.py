import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from Modelo.Clientes import Clientes
from Crud.ICrud import ICrud

class CrudClientes(ICrud):
    def __init__(self):
        self.clientes = []
    
    def create(self, **kwargs):
        nuevo_cliente = Clientes(kwargs["nombre_cliente"], kwargs["cedula_cliente"])
        self.clientes.append(nuevo_cliente)
        mensaje = "Cliente creado exitosamente"
        return {"Mensaje": mensaje, "Cliente": nuevo_cliente}

    def read(self):
        clientes = self.clientes 
        return clientes
    
    def buscar(self,cedula_cliente=None):
        for cliente in self.clientes:
            if cedula_cliente == cliente.cedula:
                mensaje = "Cliente encontrado"
                return {"Mensaje": mensaje, "Cliente": cliente}
        
        mensaje= "No se encontró al cliente"
        return {"Mensaje": mensaje, "Cliente": None}
    
    #Agregar facturas a un cliente ya creado
    def update_factura_cliente(self, cedula_cliente = None,factura = None):
        cliente = self.buscar(cedula_cliente)
        if cliente["Cliente"] != None:
            cliente["Cliente"].asociar_factura(factura)
            mensaje= "Se actualizó correctamente las facturas del cliente"
            return {"Mensaje": mensaje, "Cliente": cliente["Cliente"]}
        else:
            mensaje= "No se encontró al cliente"
            return {"Mensaje": mensaje, "Cliente": None}

    def delete_cliente(self, cedula_cliente = None):
        cliente = self.buscar(cedula_cliente)
        if cliente["Cliente"] != None:
            self.clientes.remove(cliente["Cliente"])
            mensaje= "Se eliminó correctamente el cliente"
            return {"Mensaje": mensaje, "Cliente": cliente["Cliente"]}
        else:
            mensaje= "No se encontró al cliente"
            return {"Mensaje": mensaje, "Cliente": None}












