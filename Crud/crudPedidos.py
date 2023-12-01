import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from Modelo.Pedidos import Pedidos
from Crud.ICrud import ICrud

class CrudPedidos(ICrud):

    def create_factura(self):
        nueva_factura = Pedidos()
        mensaje = "Factura creada exitosamente"
        return {"Mensaje": mensaje, "Factura": nueva_factura}

    def actualizar_productos_control(factura, producto_control):
        factura.asociar_producto_control(producto_control)
        mensaje = "Producto añadido correctamente a la factura"
        return {"Mensaje": mensaje, "Factura": factura}

    def actualizar_antibiotico(factura, producto_control):
        factura.asociar_producto_control(producto_control)
        mensaje = "Producto añadido correctamente a la factura"
        return {"Mensaje": mensaje, "Factura": factura}

    

