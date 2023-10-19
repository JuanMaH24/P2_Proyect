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
  3.2  Crear una factura CRUD
  3.3  Asociar factura al cliente CRUD

  
MENU

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
import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)


def menu(opcion):

    def verificar_numero(num):
        try:
            num=float(num)
            return True
        except ValueError:
            return False
    print("1.Desplegar opciones para Clientes")
    print("2.Desplegar opciones para manejo de Productos")
    print("3.Desplegar opciones para manejo Antibioticos")
    opcion= input("Ingrese una opcion para deplegar las opciones de acuerdoa a su necesidad:")
    if verificar_numero(opcion) == True:
        if opcion == "1": 
            
        elif opcion == "2":
       
        elif opcion == "3":

        elif opcion == "4":

        else:
            print("Gracias por usar nuestros servicios")
    else:
        print("Opcion invalida, ingrese una opcion valida.")
menu(0)