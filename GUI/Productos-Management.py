from PyQt5  import  QtWidgets, uic
import main 
from GUI import GUIManagement
app = QtWidgets.QApplication([])


menu_productos = uic.loadUi("GUI/Templates/menu-producto-control.ui")
tipo_producto_control= uic.loadUi("GUI/Templates/tipo-producto-control.ui")
agregar_producto_control = uic.loadUi("GUI/Templates/agregar-producto-control.ui")
eliminar_producto = uic.loadUi("GUI/Templates/elimminar-producto.ui")
ver_productos_control = uic.loadUi("GUI/Templates/ver-productos-control.ui")
actualizar_producto = uic.loadUi("GUI/Templates/actualizar-producto.ui")
tipo_producto_control2= uic.loadUi("GUI/Templates/tipo-producto-control.ui")
pop_up_temp = uic.loadUi("GUI/Templates/pop-up.ui")



# definir funciones activadas por los botones
def tipo_producto_control_ventana():
    menu_productos.hide()
    tipo_producto_control.show()


def agregar_producto_control_ventana(tipo):
    tipo_producto_control.hide()
    agregar_producto_control.show()
    nuevo_producto(tipo)

def eliminar_producto_ventana():
    menu_productos.hide()
    eliminar_producto.show()
    

def ver_productos_control_ventana():
    menu_productos.hide()
    ver_productos_control.show()
    todos_productos = main.productos_control()
    visualizar_productos(todos_productos)

def actualizar_producto_ventana(tipo):
    tipo_producto_control2.hide()
    actualizar_producto.show()
    actu_productos(tipo)

def pop_up(mensaje):
    pop_up_temp.mensajeRetorno.setText(mensaje)
    pop_up_temp.show()

def volver_menu_principal(ventana):
    GUIManagement.volver(ventana)

tipo_producto_control.fertilizanteBoton.clicked.connect(agregar_producto_control_ventana("fertilizante"))
tipo_producto_control.plagaBoton.clicked.connect(agregar_producto_control_ventana("plaga"))
menu_productos.nuevoProductoBoton.clicked.connect(tipo_producto_control_ventana)
menu_productos.eliminarProductoBoton.clicked.connect(eliminar_producto_ventana)
menu_productos.verProductosBoton.clicked.connect(ver_productos_control_ventana)
menu_productos.actualizarProductoBoton.clicked.connect(tipo_producto_control_ventana)
tipo_producto_control2.fertilizanteBoton.clicked.connect(actualizar_producto_ventana("fertilizante"))
tipo_producto_control2.plagaBoton.clicked.connect(actualizar_producto_ventana("plaga"))


# Menu Productos ##################################################

def nuevo_producto(tipo):
    if tipo == "fertilizante":
        tipo_propiedad="Ultima Aplicacion"
        agregar_producto_control_ventana.propiedadTipoLabel.setText(tipo_propiedad)
    else:
        tipo_propiedad="Periodo de Carencia"
        agregar_producto_control_ventana.propiedadTipoLabel.setText(tipo_propiedad)
    
    registroICA= agregar_producto_control.registroICAInput.text()
    frecuenciaAplicacion=  agregar_producto_control.frecenciaApInput.text()
    valorProducto=  agregar_producto_control.valorProductoInput.text()
    nombreProducto= agregar_producto_control.nombreProductoInput.text()
    propiedadTipo= agregar_producto_control.propiedadProductoInput.text()
    mensaje_retorno = main.nuevo_producto(registroICA,frecuenciaAplicacion,valorProducto,nombreProducto,propiedadTipo, tipo)
    pop_up(mensaje_retorno)
    volver_menu_principal(agregar_producto_control)

agregar_producto_control.agregarProductoBoton.clicked.connect(nuevo_producto)
agregar_producto_control.volverMenuBoton.clicked.connect(volver_menu_principal(agregar_producto_control))

def borrar_producto():
    registroICA= eliminar_producto.registroICAInput.text()
    mensaje_retorno= main.borrar_producto( registroICA)
    pop_up(mensaje_retorno)
    eliminar_producto.hide()
    volver_menu_principal(eliminar_producto) 

eliminar_producto.eliminarProductoBoton.clicked.connect(borrar_producto)
eliminar_producto.volverMenuBoton.clicked.connect(volver_menu_principal(eliminar_producto))


def visualizar_productos(lista_productos):
    for producto in lista_productos:
        ver_productos_control.listWidget.addItem(f"{producto.registro_ICA} -- {producto.nombre_producto} -- {producto.valor_producto}")

ver_productos_control.volverMenuBoton.clicked.connect(volver_menu_principal(ver_productos_control))

def actu_productos():
    if tipo == "fertilizante":
        tipo="Ultima Aplicacion"
        actualizar_producto_ventana.propiedadTipoLabel.setText(tipo)
    else:
        tipo="Periodo de Carencia"
        actualizar_producto_ventana.propiedadTipoLabel.setText(tipo)
    registroICA= actualizar_producto.registroICAInput.text()
    producto_buscado= main.buscar_producto(registroICA)
    if(producto_buscado is not None):
        actualizar_producto.registroICAInput.setText(registroICA)
        actualizar_producto.valorProductoInput.setText(producto_buscado.valor_producto)
        actualizar_producto.frecuenciaApInput.setText(producto_buscado.frecuencia_aplicacion)
        actualizar_producto.nombreProductoInput.setText(producto_buscado.nombre_producto)
        if tipo== "Ultima Aplicacion":
            actualizar_producto.propiedadProductoInput.setText(producto_buscado.ultima_aplicacion)
        else:
            actualizar_producto.propiedadProductoInput.setText(producto_buscado.periodo_carencia)
    else:
        pop_up("El producto no existe")
        volver_menu_principal(actualizar_producto) 

def actu2_productos():
    registro_ICA = actualizar_producto.registroICAInput.text()
    nombre_producto = actualizar_producto.nombreProductoInput.text()
    frecuencia = actualizar_producto.frecuenciaApInput.text()
    valor_producto = actualizar_producto.valorProductoInput.text()
    propiedad_tipo = actualizar_producto.propiedadProductoInput.text()
    mensaje_retorno = main.actualizar_productos(registro_ICA, nombre_producto, frecuencia, valor_producto, propiedad_tipo)
    pop_up(mensaje_retorno)
    volver_menu_principal(actualizar_producto)
    
actualizar_producto.buscarProductoBoton.clicked.connect(actu_productos)
actualizar_producto.actualizarProductoBoton.clicked.connect(actu2_productos)
actualizar_producto.volverMenuBoton.clicked.connect(volver_menu_principal(actualizar_producto))








































