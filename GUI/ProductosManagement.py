import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5  import  QtWidgets, uic
import main 
app = QtWidgets.QApplication([])


class ProductosManagement():
    
    def __init__(self):
        self.menu_productos = uic.loadUi("GUI/Templates/menu-producto-control.ui")
        self.menu_principal = self.menu_productos
        self.tipo_producto_control= uic.loadUi("GUI/Templates/tipo-producto-control.ui")
        self.agregar_producto_control = uic.loadUi("GUI/Templates/agregar-producto-control.ui")
        self.eliminar_producto = uic.loadUi("GUI/Templates/eliminar-producto.ui")
        self.ver_productos_control = uic.loadUi("GUI/Templates/ver-productos-control.ui")
        self.actualizar_producto = uic.loadUi("GUI/Templates/actualizar-producto.ui")
        self.tipo_producto_control2= uic.loadUi("GUI/Templates/tipo-producto-control.ui")
        self.pop_up_temp = uic.loadUi("GUI/Templates/pop-up.ui")
        self.menu_productos.nuevoProductoBoton.clicked.connect(self.tipo_producto_control_ventana)
        self.menu_productos.eliminarProductoBoton.clicked.connect(self.eliminar_producto_ventana)
        self.menu_productos.verProductosBoton.clicked.connect(self.ver_productos_control_ventana)
        self.menu_productos.actualizarProductoBoton.clicked.connect(self.tipo_producto_control_ventana)
        self.menu_productos.volverMenuBoton.clicked.connect(lambda: self.volver_menu_principal(self.agregar_producto_control))
        self.tipo_producto_control.volverMenuBoton.clicked.connect(lambda: self.volver_menu_principal(self.agregar_producto_control))
        self.tipo_producto_control2.volverMenuBoton.clicked.connect(lambda: self.volver_menu_principal(self.agregar_producto_control))
        self.agregar_producto_control.agregarProductoBoton.clicked.connect(self.nuevo_producto)
        self.agregar_producto_control.volverMenuBoton.clicked.connect(lambda: self.volver_menu_principal(self.agregar_producto_control))
        self.eliminar_producto.eliminarProductoBoton.clicked.connect(self.borrar_producto)
        self.eliminar_producto.volverMenuBoton.clicked.connect(lambda: self.volver_menu_principal(self.eliminar_producto))
        self.ver_productos_control.volverMenuBoton.clicked.connect(lambda: self.volver_menu_principal(self.ver_productos_control))
        self.actualizar_producto.buscarProductoBoton.clicked.connect(self.actu_productos)
        self.actualizar_producto.actualizarProductoBoton.clicked.connect(self.actu2_productos)
        self.actualizar_producto.volverMenuBoton.clicked.connect(lambda: self.volver_menu_principal(self.actualizar_producto))
        self.tipo_producto_control.fertilizanteBoton.clicked.connect(lambda: self.agregar_producto_control_ventana("fertilizante"))
        self.tipo_producto_control.plagaBoton.clicked.connect(lambda: self.agregar_producto_control_ventana("plaga"))
        self.tipo_producto_control2.fertilizanteBoton.clicked.connect(lambda: self.actualizar_producto_ventana("fertilizante"))
        self.tipo_producto_control2.plagaBoton.clicked.connect(lambda: self.actualizar_producto_ventana("plaga"))

    def mostrar_menu_productos(self, menu_principal):
        self.menu_productos.show()
        self.menu_principal = menu_principal

    # definir funciones activadas por los botones
    def tipo_producto_control_ventana(self):
        self.menu_productos.hide()
        self.tipo_producto_control.show()


    def agregar_producto_control_ventana(self, tipo):
        self.tipo_producto_control.hide()
        self.agregar_producto_control.show()
        if tipo == "fertilizante":
            tipo_propiedad="Ultima Aplicacion"
            self.agregar_producto_control.propiedadTipoLabel.setText(tipo_propiedad)
        else:
            tipo_propiedad="Periodo de Carencia"
            self.agregar_producto_control.propiedadTipoLabel.setText(tipo_propiedad)
        print("este que es el anterior creoooo que solo se ejecuta una vez, no tendría sentido aun asi no deberia pasar nada")
        self.agregar_producto_control.agregarProductoBoton.clicked.connect(self.nuevo_producto)

    def eliminar_producto_ventana(self):
        self.menu_productos.hide()
        self.eliminar_producto.show()
        

    def ver_productos_control_ventana(self):
        self.menu_productos.hide()
        self.ver_productos_control.show()
        todos_productos = main.productos_control()
        self.visualizar_productos(todos_productos)

    def actualizar_producto_ventana(self, tipo):
        self.tipo_producto_control2.hide()
        self.actualizar_producto.show()
        self.actu_productos(tipo)

    def pop_up(self, mensaje):
        self.pop_up_temp.mensajeRetorno.setText(mensaje)
        self.pop_up_temp.show()

    def volver_menu_principal(self, ventana):
        ventana.hide()
        self.menu_principal.show()



    # Menu Productos ##################################################

    def nuevo_producto(self):
        print("Osea esto en este momento se esta ejecutando")
        registroICA= self.agregar_producto_control.registroICAInput.text()
        frecuenciaAplicacion=  self.agregar_producto_control.frecuenciaApInput.text()
        valorProducto=  self.agregar_producto_control.valorProductoInput.text()
        nombreProducto= self.agregar_producto_control.nombreProductoInput.text()
        propiedadTipo= self.agregar_producto_control.propiedadProductoInput.text()
        mensaje_retorno = main.nuevo_producto(registroICA,frecuenciaAplicacion,valorProducto,nombreProducto,propiedadTipo, "fertilizante")
        self.pop_up(mensaje_retorno)
        self.volver_menu_principal(self.agregar_producto_control)


    def borrar_producto(self):
        registroICA= self.eliminar_producto.registroICAInput.text()
        mensaje_retorno= main.borrar_producto( registroICA)
        self.pop_up(mensaje_retorno)
        self.eliminar_producto.hide()
        self.volver_menu_principal(self.eliminar_producto) 



    def visualizar_productos(self, lista_productos):
        self.ver_productos_control.listWidget.clear()
        for producto in lista_productos:
            self.ver_productos_control.listWidget.addItem(f"{producto.registro_ICA} -- {producto.nombre_producto} -- {producto.valor_producto}")


    def actu_productos(self):
        if tipo == "fertilizante":
            tipo="Ultima Aplicacion"
            self.actualizar_producto_ventana.propiedadTipoLabel.setText(tipo)
        else:
            tipo="Periodo de Carencia"
            self.actualizar_producto_ventana.propiedadTipoLabel.setText(tipo)
        registroICA= self.actualizar_producto.registroICAInput.text()
        producto_buscado= main.buscar_producto(registroICA)
        if(producto_buscado is not None):
            self.actualizar_producto.registroICAInput.setText(registroICA)
            self.actualizar_producto.valorProductoInput.setText(producto_buscado.valor_producto)
            self.actualizar_producto.frecuenciaApInput.setText(producto_buscado.frecuencia_aplicacion)
            self.actualizar_producto.nombreProductoInput.setText(producto_buscado.nombre_producto)
            if tipo== "Ultima Aplicacion":
                self.actualizar_producto.propiedadProductoInput.setText(producto_buscado.ultima_aplicacion)
            else:
                self.actualizar_producto.propiedadProductoInput.setText(producto_buscado.periodo_carencia)
        else:
            self.pop_up("El producto no existe")
            self.volver_menu_principal(self.actualizar_producto) 

    def actu2_productos(self):
        registro_ICA = self.actualizar_producto.registroICAInput.text()
        nombre_producto = self.actualizar_producto.nombreProductoInput.text()
        frecuencia = self.actualizar_producto.frecuenciaApInput.text()
        valor_producto = self.actualizar_producto.valorProductoInput.text()
        propiedad_tipo = self.actualizar_producto.propiedadProductoInput.text()
        mensaje_retorno = main.actualizar_productos(registro_ICA, nombre_producto, frecuencia, valor_producto, propiedad_tipo)
        self.pop_up(mensaje_retorno)
        self.volver_menu_principal(self.actualizar_producto)