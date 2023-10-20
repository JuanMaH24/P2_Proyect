import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)
import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from Crud.crudAntibioticos import CrudAntibiotico
from Crud.crudClientes import CrudClientes
from Crud import crudPedidos

from Crud.crudProductosControl import CrudProductosControl

clientes = CrudClientes()
productos = CrudProductosControl()
antibioticos = CrudAntibiotico()

def verificar_numero(num):
    try:
        num=float(num)
        return True
    except ValueError:
        print("\nINGRESA SOLO NUMEROS EN ESTE CAMPO\n")
        return False
    
def menu_opciones(opcion):
    while opcion != "4":
        print("\n\n--------------BIENVENIDO A NUESTRO MENU-------------------")
        print("1.Desplegar opciones para Clientes")
        print("2.Desplegar opciones para manejo de Productos de Control")
        print("3.Desplegar opciones para manejo Antibioticos")
        print("4.Salir del programa\n\n") 
        opcion = input("Ingrese una opcion para deplegar las opciones de acuerdoa a su necesidad:")
        if (verificar_numero(opcion) == True) :
            if opcion == "1": 
                operaciones_clientes(0)
            elif opcion == "2":
                operaciones_productos(0)
            elif opcion == "3":
                operaciones_antibioticos(0)
            elif opcion == "4":
                print("Gracias por usar nuestros servicios")
            else:
                print("Opcion invalida, ingrese una opcion valida.")
        else:
            print("Opcion invalida, ingrese una opcion valida.")

#--------------------------------------------------------------------------------------    
def operaciones_clientes(opcion2):
    while opcion2 != "6":
        print("\n\n--------------OPCIONES CLIENTES-------------------")
        print("1.Crear un Pedido (factura)")
        print("2.Crear Cliente")
        print("3.Visualizar Clientes con sus pedidos")
        print("4.Buscar un Cliente")
        print("5.Eliminar Cliente")
        print("6.Regresar al menu principal") 
        opcion2= input("Ingrese una opcion:")
        if verificar_numero(opcion2) == True:
            if opcion2 == "1":
                crear_pedido()
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
#------------------------------------------------------------------------------------------------------
def operaciones_productos(opcion2):
    while opcion2 != "5": 
        print("\n\n--------------OPCIONES PRODUCTOS CONTROL-------------------")
        print("1.Añadir nuevos productos")
        print("2.Visualizar Porductos de control.")
        print("3.Actualizar un producto de control")
        print("4.Eliminar producto de control")
        print("5.Regresar al menu principal") 
        opcion2= input("Ingrese una opcion:")
        if verificar_numero(opcion2) == True:
            if opcion2 == "1":
                crear_producto()
            elif opcion2 == "2":
                visualizar_productos()
            elif opcion2 == "3":
                actualizar_producto()
            elif opcion2 == "4": 
                eliminar_producto()
            elif opcion2== "5":
                menu_opciones(0)
            
        else: 
            print("Opcion invalida, ingrese una opcion valida.")      
#-----------------------------------------------------------------------------------------------
def operaciones_antibioticos(opcion2):
    while opcion2 != "4":
        print("\n\n--------------OPCIONES ANTIBIOTICOS-------------------")
        print("1.Crear un antibiotico")
        print("2.Visualizar todos los anbioticos")
        print("3.Eliminar Antibiotico")
        print("4.Regresar al menu principal") 
        opcion2= input("Ingrese una opcion:")
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


"""
Acccion: Crear factura
1. pedimos ingresar la cedula del cliente
2. buscar cedula
3 Si existe el cliente
  3.1  Crear una factura CRUD
  3.2  Asociar factura al cliente CRUD
 
"""
def crear_Cliente():
    cedula_cliente= input("Ingrese la cedula del cliente:")
    while verificar_numero(cedula_cliente) == False :
        cedula_cliente= input("Ingrese la cedula del cliente:")  

    nombre_cliente= input("Ingrese el nombre del cliente:")
    
    cliente_buscado = clientes.buscar_cedula(cedula_cliente)
    if cliente_buscado["Cliente"] != None:
        if cliente_buscado["Cliente"].cedula == cedula_cliente:
            print(cliente_buscado["Mensaje"])
            print("Este cliente ya existe \n")
    else:
        cliente_creado=clientes.create_cliente(nombre_cliente,cedula_cliente)
        print(cliente_creado["Mensaje"])

def mostrar_cliente(cliente):
    print(cliente.nombre_cliente + " identificado con el número: " + cliente.cedula)
    for facturas_cliente in cliente.factura:
        print("Factura del " + str(facturas_cliente.fecha_factura) + ": \n")

        for producto_control_factura in facturas_cliente.producto_control:
            print("Producto Id: "+ str(producto_control_factura.registro_ICA))
            print("Nombre: " + str(producto_control_factura.nombre_producto))
            print("Precio: " + str(producto_control_factura.valor_producto))
            
        for producto_antibiotico in facturas_cliente.antibiotico:
            print("Nombre:"+ str(producto_antibiotico.nombre_producto))
            print("Tipo Animal: " + str(producto_antibiotico.tipo_animal))
            print("Precio: "+ str(producto_antibiotico.valor_producto))
    

def visualizar_clientes():
    if len(clientes.read()) == 0:
        print("No existen clientes registrados")
    for cliente in clientes.read():
        mostrar_cliente(cliente)

def buscar_cliente():
    cedula_cliente=input("Ingrese la cedula del cliente que desea buscar")
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

#----------------------------------------------------------------------------------------------------

def crear_producto():
    tipo_producto= str(input("¿Qué tipo de producto desea crear?\nPara producto tipo control plagas, escriba CP\nPara producto tipo fertilizante, escriba F: \n")).upper()
    registro_ICA = str(input("\nIngrese el registro ICA del control de plagas: "))
    nombre_producto= input("\nIngrese el nombre del control de plagas: ")
    frecuencia_aplicacion = input("\nIngrese la frecuencia de aplicacion: ")
    while verificar_numero(frecuencia_aplicacion) == False :
        frecuencia_aplicacion = input("Ingrese la frecuencia de aplicacion: ")
    valor_producto = input("\nIngrese el valor del producto: ")
    while verificar_numero(valor_producto) == False :
        valor_producto = input("Ingrese el valor del producto:")
        
    if tipo_producto == "CP":        
        ultima_aplicacion =input("\nIngrese hace cuantos días fue la última aplicacion valor:")
        while verificar_numero(ultima_aplicacion) == False :
            ultima_aplicacion =input("Ingrese hace cuantos días fue la última aplicacion valor:")
    
        producto_buscado = productos.buscar_producto_control(registro_ICA)
        if producto_buscado["Producto_control"] != None:
            if producto_buscado["Producto_control"].registro_ICA == registro_ICA:
                print(producto_buscado["Mensaje"])
                print("Este producto ya existe \n")
        else:
            producto_creado = productos.create_control_plagas(registro_ICA,nombre_producto, frecuencia_aplicacion, int(valor_producto),ultima_aplicacion)
            if producto_creado["Producto_control"] == None:
                print(producto_creado["Mensaje"])
    
    elif tipo_producto == "F": 
        periodo_de_carencia =input("\nIngrese hace el número de días que deben transcurrir entre la ultima aplicacion y la cosecha:")
        while verificar_numero(periodo_de_carencia) == False :
            periodo_de_carencia =input("Ingrese hace el número de días que deben transcurrir entre la ultima aplicacion y la cosecha:")
        producto_buscado = productos.buscar_producto_control(registro_ICA)
        if producto_buscado["Producto_control"] != None:
            if producto_buscado["Producto_control"].registro_ICA == registro_ICA:
                print(producto_buscado["Mensaje"])
                print("Este producto ya existe \n")
        else:
            producto_creado = productos.create_control_fertilizante(registro_ICA,nombre_producto,frecuencia_aplicacion,int(valor_producto),periodo_de_carencia)
            if producto_creado["Producto_control"] == None:
                print(producto_creado["Mensaje"])
    else:
        print("Ingrese un tipo de producto valido")
    
def mostrar_producto(producto):
    print("\nRegistro ICA: " + producto.registro_ICA)
    print("\nNombre Producto: " + producto.nombre_producto)
    print("\nFrecuencia Aplicación:" + producto.frecuencia_aplicacion)
    print("\nValor del Producto: " + str(producto.valor_producto))
    try:
        print("\nPeriodo Carencia: " + producto.periodo_carencia)
    except:
        print("\nUltima aplicacion: " + producto.ultima_aplicacion)


def visualizar_productos():
    i = 1
    for producto in productos.read_productos_control():
        print(f"Producto n.{i}")
        mostrar_producto(producto)
        i += 1

def actualizar_producto():
    registro_ICA = str(input("Ingrese el registro ICA del producto que desea actualizar"))
    producto_buscado = productos.update_producto_control(registro_ICA)
    if producto_buscado["Producto_control"] != None:
        nombre_producto= input("\nIngrese el nuevo nombre del producto de control: ")
        frecuencia_aplicacion = input("\nIngrese la nueva frecuencia de aplicacion: ")
        while verificar_numero(frecuencia_aplicacion) == False :
            frecuencia_aplicacion = input("Ingrese la nueva frecuencia de aplicacion: ")
        valor_producto = input("\nIngrese el nuevo valor del producto: ")
        while verificar_numero(valor_producto) == False :
            valor_producto = input("Ingrese el nuevo valor del producto:")
        try:
            periodo_de_carencia = producto_buscado["Producto_control"].periodo_carencia
            periodo_de_carencia =input("\nIngrese hace el nuevo número de días que deben transcurrir entre la ultima aplicacion y la cosecha:")
            while verificar_numero(periodo_de_carencia) == False :
                periodo_de_carencia =input("Ingrese hace el número de días que deben transcurrir entre la ultima aplicacion y la cosecha:")
            produc_actualizado=productos.update_producto_control(registro_ICA, nombre_producto, frecuencia_aplicacion, valor_producto, periodo_de_carencia)
            print("\n" + str (produc_actualizado["Mensaje"]))
        except:
            ultima_aplicacion = producto_buscado["Producto_control"].ultima_aplicacion
            ultima_aplicacion =input("\nIngrese hace cuantos días fue la última aplicacion:")
            while verificar_numero(ultima_aplicacion) == False :
                ultima_aplicacion =input("Ingrese hace cuantos días fue la última aplicacion:")
            produc_actualizado= productos.update_producto_control(registro_ICA, nombre_producto, frecuencia_aplicacion, valor_producto, ultima_aplicacion)
            print("\n" + str (produc_actualizado["Mensaje"]))

def eliminar_producto():
    registro_ICA = input("Ingrese el registro ICA del producto que desea eliminar")
    producto_buscado = productos.update_producto_control(registro_ICA)
    if producto_buscado["Producto_control"] != None:
        producto_eliminado = productos.delete_producto_control(registro_ICA)        
        print("\n" + str (producto_eliminado["Mensaje"]))
    else:
        print("Este producto no existe")

#-----------------------------------------------------------------------------------------

def crear_antibioticos():
    nombre_producto= str(input("Ingrese el nombre del antibiotico que desea crear:")).upper()
    antibiotico_buscado = antibioticos.buscar_antibioticos(nombre_producto)
    if antibiotico_buscado["Antibiotico"].nombre_producto == nombre_producto:
        print(antibiotico_buscado["Mensaje"])
        print("Este cliente ya existe \n")
    else:
        dosis_antibiotico = input("Ingrese la dosis del control de plagas, recuerde que debe ser mayor o igual a 400 o menor o igual a 600:")
        tipo_animal=  input("Ingrese el tipo de animal, reduerde que solo pueden ser:'BOVINO', 'PORCINO', 'CAPRINO'")
        valor_producto = input("\nIngrese el valor del producto: ")
        while verificar_numero(valor_producto) == False :
            valor_producto = input("Ingrese el valor del producto:")
        antibiotico_creado = antibioticos.create_antibiotico(nombre_producto,dosis_antibiotico,tipo_animal,int(valor_producto))
        print("\n" + str (antibiotico_creado["Mensaje"]))

def mostrar_antibiotico(antibiotico):
    print("\nNombre Producto: " + antibiotico.nombre_producto)
    print("\nDosis:" + antibiotico.dosis_antibiotico)
    print("\nTipo de animal:" + antibiotico.tipo_animal)
    print("\nValor del Producto: " + str(antibiotico.valor_producto))

def visualizar_antibioticos():
    i = 1
    for antibiotico in antibioticos.read():
        print(f"\nAntibiotico n.{i}")
        mostrar_antibiotico(antibiotico)
        i += 1   


def eliminar_antibioticos():
    nombre_producto= str(input("Ingrese el nombre del antibiotico que desea eliminar:")).upper()
    antibiotico_buscado = antibioticos.buscar_antibioticos(nombre_producto)
    if antibiotico_buscado["Antibiotico"].nombre_producto == nombre_producto:
        antibiotico_eliminado= antibioticos.delete_antibiotico(nombre_producto)
        print("\n" + str (antibiotico_eliminado["Mensaje"]))
    else:
        print("Este producto no existe")

#-------------------------------------------------------------------------------------------
def crear_pedido():
    cedula_cliente= input("Ingrese la cedula del cliente:")
    while verificar_numero(cedula_cliente) == False :
        cedula_cliente= input("Ingrese la cedula del cliente:") 
    cliente_buscado = clientes.buscar_cedula(cedula_cliente)
    if cliente_buscado["Cliente"] != None:
        factura_creada = crudPedidos.create_factura()
        opcion_productos = "S"
        while opcion_productos == "S":
            tipo_producto = str(input("¿Qué tipo de producto desea ingresa?.\nPara ANTIBIOTICO ingrese A\nPara producto de contro ingrese PC: ")).upper()
            if tipo_producto == 'A':       
                nombre_producto= str(input("\nIngrese el nombre del antibiotico que desea añadir a la facura:")).upper()
                antibiotico_buscado = antibioticos.buscar_antibioticos(nombre_producto)
                if antibiotico_buscado["Antibiotico"] != None:
                    factura_creada = crudPedidos.actualizar_antibiotico(factura_creada["Factura"],antibiotico_buscado["Antibiotico"])
                else: 
                    print("No se puede añadir, ya que no se encontró este antibiotico")
            elif tipo_producto == 'PC':           
                registro_ICA = str(input("\nIngrese el registro ICA del producto que desea añadir a la factura:")).upper()
                registro_buscado = productos.buscar_producto_control(registro_ICA)
                if registro_buscado["Producto_control"] != None:
                    factura_creada = crudPedidos.actualizar_productos_control(factura_creada["Factura"], registro_buscado["Producto_control"])
                else:
                    print("\nEste producto no existe")
            else:
                print("\nEl tipo ingresado de producto no existe")

            opcion_productos = str(input("\nDesea añadir mas productos a la factura?:"))
        clientes.update_factura_cliente(cedula_cliente,factura_creada["Factura"])
        print("\nFactura creada y asociada correctamente")
    else:
        print(cliente_buscado["Mensaje"])
        print("No puede crear una factura sin un cliente ya creado \n")