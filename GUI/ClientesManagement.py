import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5  import  QtWidgets, uic
import main 
app = QtWidgets.QApplication([])

class ClientesManagement():
    def __init__(self):
        self.menu_clientes = uic.loadUi("GUI/Templates/menu-clientes.ui")
        self.menu_principal = self.menu_clientes
        self.pedido_form = uic.loadUi("GUI/Templates/pedido-form.ui")
        self.agregar_cliente = uic.loadUi("GUI/Templates/agregar-cliente.ui")
        self.eliminar_cliente = uic.loadUi("GUI/Templates/eliminar-cliente.ui")
        self.ver_cliente = uic.loadUi("GUI/Templates/ver-cliente.ui")
        self.ver_todos_clientes = uic.loadUi("GUI/Templates/ver-todos-clientes.ui")
        self.pop_up_temp = uic.loadUi("GUI/Templates/pop-up.ui")


        self.todos_clientes = []
        self.menu_clientes.hacerPedidoBoton.clicked.connect(self.hacer_pedido_ventana)
        self.menu_clientes.registrarClienteBoton.clicked.connect(self.registrar_cliente_ventana)
        self.menu_clientes.verClientesBoton.clicked.connect(self.ver_todos_clientes_ventana)
        self.menu_clientes.buscarClienteBoton.clicked.connect(self.buscar_cliente_ventana)
        self.menu_clientes.eliminarClienteBoton.clicked.connect(self.eliminar_cliente_ventana)

        self.productos_agregados=[]

        self.pedido_form.agregarFacturaBoton.clicked.connect(self.agregar_producto_factura)
        self.pedido_form.realizarPedidoBoton.clicked.connect(self.realizar_pedido)
        self.pedido_form.volverMenuBoton.clicked.connect(lambda: self.volver_menu_principal(self.pedido_form))
        self.agregar_cliente.agregarClienteBoton.clicked.connect(self.nuevo_cliente)
        self.agregar_cliente.volverMenuBoton.clicked.connect(lambda: self.volver_menu_principal(self.agregar_cliente))
        self.ver_todos_clientes.siguienteClienteBoton.clicked.connect(self.siguiente_cliente)
        self.ver_todos_clientes.volverMenuBoton.clicked.connect(lambda: self.volver_menu_principal(self.ver_todos_clientes))
        self.ver_cliente.buscarClienteBoton.clicked.connect(self.visualizar_cliente)
        self.ver_cliente.volverMenuBoton.clicked.connect(lambda: self.volver_menu_principal(self.ver_cliente))
        self.eliminar_cliente.eliminarClienteBoton.clicked.connect(self.borrar_cliente)
        self.eliminar_cliente.volverMenuBoton.clicked.connect(lambda: self.volver_menu_principal(self.eliminar_cliente))
        
    def mostrar_menu_cliente(self, menu_principal):
        self.menu_clientes.show()
        self.menu_principal = menu_principal
        
    # definir funciones activadas por los botones
    def hacer_pedido_ventana(self):
        self.menu_clientes.hide()
        self.pedido_form.productoElegido.addItems([producto.nombre_producto for producto in main.productos_inventario()])
        self.pedido_form.show()
        

    def registrar_cliente_ventana(self):
        self.menu_clientes.hide()
        self.agregar_cliente.show()

    def ver_todos_clientes_ventana(self):
        self.menu_clientes.hide()
        self.ver_todos_clientes.show()
        self.todos_clientes = main.clientes_registrados().copy()
        self.visualizar_clientes(self.todos_clientes)

    def buscar_cliente_ventana(self):
        self.menu_clientes.hide()
        self.ver_cliente.show()

    def eliminar_cliente_ventana(self):
        self.menu_clientes.hide()
        self.eliminar_cliente.show()

    def pop_up(self, mensaje):
        self.pop_up_temp.mensajeRetorno.setText(mensaje)
        self.pop_up_temp.show()

    def volver_menu_principal(self, ventana):
        ventana.hide()
        self.menu_principal.show()


    # Menu clientes ##################################################
    def agregar_producto_factura(self):
        inventario = main.productos_inventario()
        producto = self.pedido_form.productoElegido.currentIndex()
        self.pedido_form.listWidget.addItem(f"{inventario[producto].nombre_producto} -- {inventario[producto].valor_producto}")
        self.productos_agregados.append((inventario[producto]))

    def realizar_pedido(self):
        # colocar un pop-up diciendo e dónde se guardó el pedido y que se realizó
        cedula = self.pedido_form.cedulaClienteInput.text()
        mensaje_retorno = main.realizar_pedido(cedula, self.productos_agregados)
        self.pop_up(mensaje_retorno)
        self.pedido_form.hide()
        self.volver_menu_principal(self.pedido_form)


    def nuevo_cliente(self):
        cedula= self.agregar_cliente.cedulaClienteInput.text()
        nombre_cliente=  self.agregar_cliente.nombreClienteInput.text()
        mensaje_retorno = main.nuevo_cliente(cedula,nombre_cliente)
        self.pop_up(mensaje_retorno)
        self.volver_menu_principal(self.agregar_cliente)

    def visualizar_facturas(self, facturas):
        self.ver_todos_clientes.listWidget.clear()
        i = 0
        for factura in facturas:
            i += 1
            self.ver_todos_clientes.listWidget.addItem(f"Factura {i}")
            for producto_control in factura.producto_control:
                self.ver_todos_clientes.listWidget.addItem(f"{producto_control.registro_ICA} -- {producto_control.nombre_producto} -- {producto_control.valor_producto}")
            for antibiotico in factura.antibiotico:
                self.ver_todos_clientes.listWidget.addItem(f"{antibiotico.nombre_producto} -- {antibiotico.tipo_animal} -- {antibiotico.valor_producto}")

    def visualizar_clientes(self, lista_clientes):
        if(len(lista_clientes) > 0):
            cedula = lista_clientes[0].cedula
            nombre = lista_clientes[0].nombre_cliente
            self.ver_todos_clientes.cedulaClienteLabel.setText(cedula)
            self.ver_todos_clientes.nombreClienteLabel.setText(nombre)
            self.visualizar_facturas(lista_clientes[0].factura)
        else:
            self.pop_up("No hay más clientes")
            self.volver_menu_principal(self.ver_todos_clientes)    

    def siguiente_cliente(self):
        self.todos_clientes.pop(0)
        self.visualizar_clientes(self.todos_clientes)

    def visualizar_cliente(self):
        cedula= self.ver_cliente.cedulaClienteInput.text()
        cliente_buscado = main.buscar_cliente(cedula)
        if(cliente_buscado is not None):
            self.ver_cliente.cedulaClienteLabel.setText(cedula)
            self.ver_cliente.nombreClienteLabel.setText(cliente_buscado.nombre)
            self.visualizar_facturas(cliente_buscado.factura)
        else:
            self.pop_up("El cliente no existe")
            self.volver_menu_principal(self.ver_cliente) 

        
    def borrar_cliente(self):
        cedula= self.eliminar_cliente.cedulaClienteInput.text()
        mensaje_retorno= main.borrar_cliente(cedula)
        self.pop_up(mensaje_retorno)
        self.volver_menu_principal(self.eliminar_cliente) 