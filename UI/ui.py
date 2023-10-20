import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)
import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from Crud.crudAntibioticos import crudAntibiotico
from Crud.crudClientes import CrudClientes
from Crud.crudPedidos import CrudPedidos
from Crud.crudProductosControl import CrudProductosControl

clientes = CrudClientes()
def verificar_numero(num):
    try:
        num=float(num)
        return True
    except ValueError:
        return False
    
def menu_opciones(opcion):
    while opcion != "4":
        print("1.Desplegar opciones para Clientes")
        print("2.Desplegar opciones para manejo de Productos")
        print("3.Desplegar opciones para manejo Antibioticos")
        print("4.Salir del programa") 
        opcion = input("Ingrese una opcion para deplegar las opciones de acuerdoa a su necesidad:")
        if (verificar_numero(opcion) == True) :
            if opcion == "1": 
                operaciones_clientes()
            elif opcion == "2":
                operaciones_productos()
            elif opcion == "3":
                operaciones_antibioticos()
            elif opcion == "4":
                print("Gracias por usar nuestros servicios")
            else:
                print("Opcion invalida, ingrese una opcion valida.")
        else:
            print("Opcion invalida, ingrese una opcion valida.")

    
def operaciones_clientes():

    print("1.Crear un Pedido (factura)")
    print("2.Crear Cliente")
    print("3.Visualizar Clientes con sus pedidos")
    print("4.Buscar un Cliente")
    print("5.Eliminar Cliente")
    print("6.Regresar al menu principal") 
    opcion2= input("Ingrese una opcion:")
    while opcion2 != "6":
        if verificar_numero(opcion2) == True:
            if opcion2 == "1":
                print("hola")
            elif opcion2 == "2":
                crear_Cliente()
            elif opcion2 == "3":
                visualizar_clientes()
            elif opcion2 == "4": 
                buscar_cliente()
            elif opcion2== "5":
                eliminar_cliente()
            elif opcion2== "6":
                menu_opciones(0)
        else: 
            print("Opcion invalida, ingrese una opcion valida.")  

def operaciones_productos():

    print("1.Añadir nuevos productos")
    print("2.Visualizar Porductos de control.")
    print("3.Buscar un producto de control")
    print("4.Actualizar un producto de control")
    print("5.Eliminar producto de control")
    print("6.Regresar al menu principal") 
    opcion2= input("Ingrese una opcion:")
    while opcion2 != "6": 
        if verificar_numero(opcion2) == True:
            if opcion2 == "1":
                print("hola")
            elif opcion2 == "2":
                print("hola")
            elif opcion2 == "3":
                print("hola")
            elif opcion2 == "4": 
                print("hola")
            elif opcion2== "5":
                menu_opciones(0)
        else: 
            print("Opcion invalida, ingrese una opcion valida.")      

def operaciones_antibioticos():

    print("1.Crear un antibiotico")
    print("2.Visualizar todos los anbioticos")
    print("3.Eliminar Antibiotico")
    print("4.Regresar al menu principal") 
    opcion2= input("Ingrese una opcion:")
    while opcion2 != "4":
        if verificar_numero(opcion2) == True:
            if opcion2 == "1":
                print("hola")
            elif opcion2 == "2":
                print("hola")
            elif opcion2 == "3":
                print("hola")
            elif opcion2 == "4": 
                menu_opciones(0)
        else: 
            print("Opcion invalida, ingrese una opcion valida.")    


#----------------------------------------------------------------------------------------------------------------
def crear_Cliente():
    cedula_cliente= input("Ingrese la cedula del cliente:")
    while verificar_numero(cedula_cliente) == False :
        cedula_cliente= input("Ingrese la cedula del cliente:")  

    nombre_cliente= input("Ingrese el nombre del cliente:")
    
    cliente_buscado = clientes.buscar_cedula(cedula_cliente)
    if cliente_buscado["Cliente"].cedula == cedula_cliente:
        print(cliente_buscado["Mensaje"])
        print("Este cliente ya existe \n")
    else:
        clientes.create_cliente(nombre_cliente,cedula_cliente)

def mostrar_cliente(cliente):
    print(cliente.nombre + " identificado con el número: " + cliente.cedula)
    for facturas_cliente in cliente.factura:
        print("Factura del " + str(facturas_cliente.fecha_factura) + ": \n")

        for producto_control_factura in facturas_cliente.producto_control:
            print("Producto Id: "+ str(producto_control_factura.registro_ICA))
            print("Nombre: " + str(producto_control_factura.nombreProducto))
            print("Precio: " + str(producto_control_factura.valor_producto))
            
        for producto_antibiotico in facturas_cliente.antibiotico:
            print("Nombre:"+ str(producto_antibiotico.nombre_producto))
            print("Tipo Animal: " + str(producto_antibiotico.tipo_animal))
            print("Precio: "+ str(producto_antibiotico.valor_producto))
    

def visualizar_clientes():
    for cliente in clientes.read():
        mostrar_cliente(cliente)

def buscar_cliente():
    cedula_cliente=print("Ingrese la cedula del cliente que desea buscar")
    while verificar_numero(cedula_cliente) == False :
        cedula_cliente= input("Ingrese la cedula del cliente:")
    cliente_buscado = clientes.buscar_cedula(cedula_cliente)
    print(cliente_buscado["Mensaje"])
    if cliente_buscado["Cliente"] != None:
        mostrar_cliente(cliente_buscado["Cliente"])

def eliminar_cliente():
    cedula_cliente=print("Ingrese la cedula del cliente que desea eliminar")
    while verificar_numero(cedula_cliente) == False :
        cedula_cliente= input("Ingrese la cedula del cliente:")
    cliente_eliminado = clientes.delete_cliente(cedula_cliente)
    print(cliente_eliminado["Mensaje"])

#---------------------------------------------------------------------------------
# def crear_producto():
#     tipo_producto=print("")

