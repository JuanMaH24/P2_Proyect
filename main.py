import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from Crud import crudAntibioticos, crudClientes, crudPedidos, crudProductosControl

clientes = crudClientes.CrudClientes()
productos = crudProductosControl.CrudProductosControl()
antibioticos = crudAntibioticos.CrudAntibiotico()

# opcion= ventanas.ventanaPrincipal()
#     if opcion == '0':

def verificar_numero(num):
    try:
        num == int(num)
        return True
    except ValueError:
        return False

def productos_inventario():
    inventario = []
    inventario.extend(productos.productos_control)
    inventario.extend(antibioticos.antibioticos)
    return inventario

def clientes_registrados():
    return clientes.clientes

def realizar_pedido(cedula, productos_agregados):
    if(verificar_numero(cedula) == True):
        cliente_buscado = clientes.buscar(cedula_cliente=cedula)
        if cliente_buscado["Cliente"] != None:
            factura_creada = crudPedidos.create()
            for producto in productos_agregados:
                factura_creada = crudPedidos.actualizar_antibiotico(factura_creada["Factura"], producto)
            
            clientes.update(cedula,factura_creada["Factura"])
            return "Factura creada y asociada correctamente"
        else:
            return "Cliente no existente"
    else:
        return "Cédula inválida"

def nuevo_cliente(cedula, nombre_cliente):
    if(verificar_numero(cedula) == True):
        cliente_buscado = clientes.buscar(cedula_cliente=cedula)
        if cliente_buscado["Cliente"] == None:
            cliente_creado = clientes.create(nombre_cliente = nombre_cliente,cedula_cliente = cedula)
            return cliente_creado["Mensaje"]
        else:
            return "Cliente Existente"
    else:
        return "Cédula inválida"
    
def buscar_cliente(cedula):
    cliente_buscado = clientes.buscar(cedula_cliente=cedula)
    return cliente_buscado["Cliente"]

def borrar_cliente(cedula):
    if(verificar_numero(cedula) == True):
        cliente_eliminado = clientes.delete(cedula_cliente = cedula)
        return cliente_eliminado["Mensaje"]
    else:
        return "Cédula inválida"



def antibioticos_existentes():
    return antibioticos.antibioticos

def nuevo_antibiotico(nombre_producto, dosis, tipo_animal, valor_producto):
    antibiotico_buscado = antibioticos.buscar(nombre_producto=nombre_producto)
    if antibiotico_buscado["Antibiotico"] != None:
        return antibiotico_buscado["Mensaje"]
    else:
        val_producto= int(valor_producto)
        if(verificar_numero(val_producto) == True):
            antibiotico_creado = antibioticos.create(nombre_producto = nombre_producto,dosis = int(dosis),tipo_animal = tipo_animal,valor_producto = int(valor_producto))
            return antibiotico_creado["Mensaje"]
        else:
            return "Val no válido"

def borrar_antibiotico(nombre):
    antibiotico_buscado = antibioticos.buscar(nombre)
    if antibiotico_buscado["Antibiotico"] != None:
        antibiotico_eliminado = antibioticos.delete(nombre_producto=nombre)
        return antibiotico_eliminado["Mensaje"]
    else:
        return "No existe"

# PRODUCTOS CONTROL #####################################################################################################################
def productos_control():
    return productos.productos_control

def nuevo_producto(registro_ICA, frecuencia_aplicacion, valor_producto, nombre_producto, propiedad_tipo, tipo):
    # if frecuencia_aplicacion == "":
    #     return "Frec. None"
    # try:
    #     frecuencia_aplicacion == int(frecuencia_aplicacion)
    # except ValueError:
    #     return "Frec.A None"
    
    # if (verificar_numero(frecuencia_aplicacion) == False):
    #     return "Frec.A None"
        
    if (verificar_numero(valor_producto) == False ): 
        return "Val. None" 


    if tipo == "fertilizante":
        if (verificar_numero(propiedad_tipo) == False):
            return "Ultima Ap. None"
        producto_buscado = productos.buscar(registro_ICA)
        if producto_buscado["Producto_control"] != None:
            return "RegistroICA existe"
        else:
            producto_creado = productos.create(registro_ICA=registro_ICA, nombre_producto=nombre_producto, frecuencia_aplicacion=int(frecuencia_aplicacion), valor_producto=int(valor_producto), propiedad_tipo=int(propiedad_tipo))
            return "Se creo"
    else:
        if (verificar_numero(propiedad_tipo) == False):
            return "P.C inválida"
        
        producto_buscado = productos.buscar(registro_ICA)
        if producto_buscado["Producto_control"] != None:
            return "El Registro ICA ya existe"
        else:
            producto_creado = productos.create_control_plagas(registro_ICA=registro_ICA, nombre_producto=nombre_producto, frecuencia_aplicacion=int(frecuencia_aplicacion), valor_producto=int(valor_producto), propiedad_tipo=int(propiedad_tipo))
            return "Se creo"
def borrar_producto(registro_ICA):
    producto_buscado = productos.buscar(registro_ICA = registro_ICA)
    if producto_buscado["Producto_control"] != None:
        producto_eliminado = productos.delete(registro_ICA)        
        return producto_eliminado["Producto_control"]
    else:
        return "Este producto no existe"
        
def buscar_producto(registro_ICA):
    producto_buscado = productos.buscar(registro_ICA = registro_ICA)
    return producto_buscado["Producto_control"]

def actualizar_productos(registro_ICA, nombre_producto, frecuencia, valor_producto, propiedad_tipo):
   
    if (frecuencia == int(frecuencia) == False):
        return "Frec. None"
    else:
        frecuencia = int(frecuencia)
    
    # if (verificar_numero(frecuencia_aplicacion) == False):
    #     return "Frec.A None"
    if (verificar_numero(valor_producto) == False ): 
        return "Val. None" 
    if (verificar_numero(propiedad_tipo) == False):
        return "Valor numerico inválido"
    produc_actualizado = productos.update_producto_control(registro_ICA, nombre_producto, frecuencia, valor_producto, propiedad_tipo)
    return produc_actualizado["Mensaje"]

        
    
    