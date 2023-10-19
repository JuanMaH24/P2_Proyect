# import pytest
import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from Crud.crudClientes import CrudClientes
from Modelo.Pedidos import Pedidos

base_info = CrudClientes()



base_info.create_cliente("Sofia Soto", "35892")
base_info.create_cliente("JuanMa Herrera", "1004")

factura1 = Pedidos()
factura1.asociar_antibiotico("supuestoa")
factura1.asociar_producto_control("supuestob")

base_info.update_factura_cliente("35892", factura1)
base_info.update_factura_cliente("35892", factura1)

base_info.update_factura_cliente("1004", "SupuestaFact4")

print(base_info.clientes[0].factura)

base_info.update_factura_cliente("35892", "SupuestaFact3")

print(base_info.clientes[0].factura)

print(base_info.read())
base_info.delete_cliente("1004")
print(base_info.read())