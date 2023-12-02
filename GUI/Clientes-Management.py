from PyQt5  import  QtWidgets, uic
import main 
from GUI import GUIManagement
app = QtWidgets.QApplication([])


menu_clientes = uic.loadUi("GUI/Templates/menu-clientes.ui")
pedido_form = uic.loadUi("GUI/Templates/pedido-form.ui")
agregar_cliente = uic.loadUi("GUI/Templates/agregar-cliente.ui")
eliminar_cliente = uic.loadUi("GUI/Templates/elimminar-cliente.ui")
ver_cliente = uic.loadUi("GUI/Templates/ver-cliente.ui")
ver_todos_clientes = uic.loadUi("GUI/Templates/ver-todos-clientes.ui")
pop_up_temp = uic.loadUi("GUI/Templates/pop-up.ui")

pedido_form.productoElegido.addItems(main.productos_inventario())

todos_clientes = []

# definir funciones activadas por los botones
def hacer_pedido_ventana():
    menu_clientes.hide()
    pedido_form.show()
    

def registrar_cliente_ventana():
    menu_clientes.hide()
    agregar_cliente.show()

def ver_todos_clientes_ventana():
    menu_clientes.hide()
    ver_todos_clientes.show()
    todos_clientes = main.clientes_registrados()
    visualizar_clientes(todos_clientes)

def buscar_cliente_ventana():
    menu_clientes.hide()
    ver_cliente.show()

def eliminar_cliente_ventana():
    menu_clientes.hide()
    eliminar_cliente.show()

def pop_up(mensaje):
    pop_up_temp.mensajeRetorno.setText(mensaje)
    pop_up_temp.show()

def volver_menu_principal(ventana):
    GUIManagement.volver(ventana)

menu_clientes.hacerPedidoBoton.clicked.connect(hacer_pedido_ventana)
menu_clientes.registrarClienteBoton.clicked.connect(registrar_cliente_ventana)
menu_clientes.verClientesBoton.clicked.connect(ver_todos_clientes_ventana)
menu_clientes.buscarClienteBoton.clicked.connect(buscar_cliente_ventana)
menu_clientes.eliminarClienteBoton.clicked.connect(eliminar_cliente_ventana)

productos_agregados=[]
# Menu clientes ##################################################
def agregar_producto_factura():
    producto = pedido_form.productoElegido.currentText()
    pedido_form.listWidget.addItem(producto)
    productos_agregados.append((producto))

def realizar_pedido():
    # colocar un pop-up diciendo e dónde se guardó el pedido y que se realizó
    cedula = pedido_form.cedulaClienteInput.text()
    mensaje_retorno = main.realizar_pedido(cedula, productos_agregados)
    pop_up(mensaje_retorno)
    pedido_form.hide()
    volver_menu_principal(pedido_form)

pedido_form.agregarFacturaBoton.clicked.connect(agregar_producto_factura)
pedido_form.realizarPedidoBoton.clicked.connect(realizar_pedido)
pedido_form.volverMenuBoton.clicked.connect(volver_menu_principal(pedido_form))


def nuevo_cliente():
    cedula= agregar_cliente.cedulaClienteInput.text()
    nombre_cliente=  agregar_cliente.nombreClienteInput.text()
    mensaje_retorno = main.nuevo_cliente(cedula,nombre_cliente)
    pop_up(mensaje_retorno)
    volver_menu_principal(agregar_cliente)

agregar_cliente.agregarClienteBoton.clicked.connect(nuevo_cliente)
agregar_cliente.volverMenuBoton.clicked.connect(volver_menu_principal(agregar_cliente))


def visualizar_facturas(facturas):
    i = 0
    for factura in facturas:
        i += 1
        ver_todos_clientes.listWidget.addItem(f"Factura {i}")
        for producto_control in factura.producto_control:
            ver_todos_clientes.listWidget.addItem(f"{producto_control.registro_ICA} -- {producto_control.nombre_producto} -- {producto_control.valor_producto}")
        for antibiotico in factura.antibiotico:
            ver_todos_clientes.listWidget.addItem(f"{antibiotico.nombre_producto} -- {antibiotico.tipo_animal} -- {antibiotico.valor_producto}")

def visualizar_clientes(lista_clientes):
    if(len(lista_clientes) > 0):
        cedula = lista_clientes[0].cedula
        nombre = lista_clientes[0].nombre_cliente
        ver_todos_clientes.cedulaClienteLabel.setText(cedula)
        ver_todos_clientes.nombreClienteLabel.setText(nombre)
        visualizar_facturas(lista_clientes[0].factura)
    else:
        pop_up("No hay más clientes")
        volver_menu_principal(ver_todos_clientes)    

def siguiente_cliente():
    todos_clientes.pop(0)
    visualizar_cliente(todos_clientes)

ver_todos_clientes.siguienteClienteBoton.clicked.connect(siguiente_cliente)
ver_todos_clientes.volverMenuBoton.clicked.connect(volver_menu_principal(ver_todos_clientes))


def visualizar_cliente():
    cedula= ver_cliente.cedulaClienteInput.text()
    cliente_buscado = main.buscar_cliente(cedula)
    if(cliente_buscado is not None):
        ver_cliente.cedulaClienteLabel.setText(cedula)
        ver_cliente.nombreClienteLabel.setText(cliente_buscado.nombre)
        visualizar_facturas(cliente_buscado.factura)
    else:
        pop_up("El cliente no existe")
        volver_menu_principal(ver_cliente) 

ver_cliente.buscarClienteBoton.clicked.connect(visualizar_cliente)
ver_cliente.volverMenuBoton.clicked.connect(volver_menu_principal(ver_cliente))

    
def borrar_cliente():
    cedula= eliminar_cliente.cedulaClienteInput.text()
    mensaje_retorno= main.borrar_cliente(cedula)
    pop_up(mensaje_retorno)
    volver_menu_principal(eliminar_cliente) 


eliminar_cliente.eliminarClienteBoton.clicked.connect(borrar_cliente)
eliminar_cliente.volverMenuBoton.clicked.connect(volver_menu_principal(eliminar_cliente))












































