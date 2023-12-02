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
        num=float(num)
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
        cliente_buscado = clientes.buscar_cedula(cedula)
        if cliente_buscado["Cliente"] != None:
            factura_creada = crudPedidos.create_factura()
            for producto in productos_agregados:
                factura_creada = crudPedidos.actualizar_antibiotico(factura_creada["Factura"], producto)
            clientes.update_factura_cliente(cedula,factura_creada["Factura"])
            return "Factura creada y asociada correctamente"
        else:
            return "Cliente no existente"
    else:
        return "Cédula inválida"

def nuevo_cliente(cedula, nombre_cliente):
    if(verificar_numero(cedula) == True):
        cliente_buscado = clientes.buscar_cedula(cedula)
        if cliente_buscado["Cliente"] == None:
            cliente_creado = clientes.create_cliente(nombre_cliente,cedula)
            return cliente_creado["Mensaje"]
        else:
            return "Cliente Existente"
    else:
        return "Cédula inválida"
    
def buscar_cliente(cedula):
    cliente_buscado = clientes.buscar_cedula(cedula)
    return cliente_buscado["Cliente"]

def borrar_cliente(cedula):
    if(verificar_numero(cedula) == True):
        cliente_eliminado = clientes.delete_cliente(cedula)
        return cliente_eliminado["Mensaje"]
    else:
        return "Cédula inválida"



def antibioticos_existentes():
    return antibioticos.antibioticos

def nuevo_antibiotico(nombre_producto, dosis, tipo_animal, valor_producto):
    antibiotico_buscado = antibioticos.buscar_antibioticos(nombre_producto)
    if antibiotico_buscado["Antibiotico"] != None:
        return antibiotico_buscado["Mensaje"]
    else:
        if(verificar_numero(valor_producto) == True):
            antibiotico_creado = antibioticos.create_antibiotico(nombre_producto,dosis,tipo_animal,int(valor_producto))
            return antibiotico_creado["Mensaje"]
        else:
            return "Valor del antibiotico no válido"

def borrar_antibiotico(nombre):
    antibiotico_buscado = antibioticos.buscar_antibioticos(nombre)
    if antibiotico_buscado["Antibiotico"] != None:
        antibiotico_eliminado = antibioticos.delete_antibiotico(nombre)
        return antibiotico_eliminado["Mensaje"]
    else:
        return "Este antibiotico no existe"

# PRODUCTOS CONTROL #####################################################################################################################
def productos_control():
    return productos.productos_control

def nuevo_producto(registro_ICA, frecuencia_aplicacion, valor_producto, nombre_producto, propiedad_tipo, tipo):
    if (verificar_numero(frecuencia_aplicacion) == False ): 
            return "Frecuencia de aplicación inválida"
        
    if (verificar_numero(valor_producto) == False ): 
        return "Valor inválido" 

    if tipo == "fertilizante":
        if (verificar_numero(propiedad_tipo) == False):
            return "Ultima aplicación inválida"
        
        producto_buscado = productos.buscar_producto_control(registro_ICA)
        if producto_buscado["Producto_control"] != None:
            return "El Registro ICA ya existe"
        else:
            producto_creado = productos.create_control_fertilizante(registro_ICA,nombre_producto,frecuencia_aplicacion,int(valor_producto),propiedad_tipo)
            return producto_creado["Producto_control"]
    else:
        if (verificar_numero(propiedad_tipo) == False):
            return "Periodo de carencia inválida"
        
        producto_buscado = productos.buscar_producto_control(registro_ICA)
        if producto_buscado["Producto_control"] != None:
            return "El Registro ICA ya existe"
        else:
            producto_creado = productos.create_control_plagas(registro_ICA,nombre_producto, frecuencia_aplicacion, int(valor_producto),propiedad_tipo)
            return producto_creado["Producto_control"]

def borrar_producto(registro_ICA):
    producto_buscado = productos.buscar_producto_control(registro_ICA)
    if producto_buscado["Producto_control"] != None:
        producto_eliminado = productos.delete_producto_control(registro_ICA)        
        return producto_eliminado["Producto_control"]
    else:
        return "Este producto no existe"
        
def buscar_producto(registro_ICA):
    producto_buscado = productos.buscar_producto_control(registro_ICA)
    return producto_buscado["Producto_control"]

def actualizar_productos(registro_ICA, nombre_producto, frecuencia, valor_producto, propiedad_tipo):
    if (verificar_numero(frecuencia) == False ): 
        return "Frecuencia de aplicación inválida"
        
    if (verificar_numero(valor_producto) == False ): 
        return "Valor inválido" 
    
    if (verificar_numero(propiedad_tipo) == False):
        return "Valor numerico inválido"

    produc_actualizado = productos.update_producto_control(registro_ICA, nombre_producto, frecuencia, valor_producto, propiedad_tipo)
    return produc_actualizado["Mensaje"]

        
    
    