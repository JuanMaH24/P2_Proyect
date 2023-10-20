"""" 
Accion: Mos
Acccion: Crear factura
1. pedimos ingresar la cedula del cliente
2. buscar cedula
3 Si existe el cliente
  3.1  Crear una factura CRUD
  3.2  Asociar factura al cliente CRUD
 
  Si no existe el cliente

  3.1 Crear un cliente CRUD
  3.2  Cr6ear una factura CRUD
  3.3  Asociar factura al cliente CRUD

"""
import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)
from UI.ui import menu_opciones

def menu():
    menu_opciones(0)
    
menu()