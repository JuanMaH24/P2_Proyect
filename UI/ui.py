import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

"""
OPCIONES CLIENTES
1. Crear un Pedido (factura)
2. Visualizar Clientes con sus pedidos
3. Crear Cliente
4. Mostrar Clientes
5. Eliminar Clientes

OPCIONES PRODUCTOS
5. Añadir productos
4. Visualizar Porductos control plagas.
   4.1 Crear fertilizantes
   4.2 Crear control plagas
   4.3 Eliminar Productos 
   
OPCIONES ANTIBIOTICOS

  5.1 Crear un antibiotico
  5.2 Visualizar todos los anbioticos
  5.3 Buscar un antibiotico
  5.4 Eliminar Antibiotico
"""
def verificar_numero(num):
    try:
        num=float(num)
        return True
    except ValueError:
        return False
    
def Operaciones_clientes(self):

  print("1.Crear un Pedido (factura)")
  print("2.Visualizar Clientes con sus pedidos")
  print("3.Crear Cliente")
  print("4.Mostrar Clientes")
  print("5.Eliminar Clientes")
  opcion2= input("Ingrese una opcion:") 
  if verificar_numero(opcion2) == True:
      if opcion2 == "1":
      elif opcion2 == "2":
      elif opcion2 == "3":
      elif opcion2 == "4": 
      elif opcion2== "5":