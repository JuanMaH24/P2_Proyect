import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5  import  QtWidgets, uic
import main 
app = QtWidgets.QApplication([])

class ManejadorAntibioticos:
    def __init__(self):
        self.menu_antibiotico = uic.loadUi("GUI/Templates/menu-antibioticos.ui")
        self.menu_principal = self.menu_antibiotico
        self.agregar_antibiotico = uic.loadUi("GUI/Templates/agregar-antibiotico.ui")
        self.ver_antibioticos = uic.loadUi("GUI/Templates/ver-antibioticos.ui")
        self.eliminar_antibiotico = uic.loadUi("GUI/Templates/eliminar-antibiotico.ui")
        self.pop_up_temp = uic.loadUi("GUI/Templates/pop-up.ui")

        self.menu_antibiotico.nuevoAntibioticoBoton.clicked.connect(self.agregar_antibiotico_ventana)
        self.menu_antibiotico.verAntibioticosBoton.clicked.connect(self.ver_antibioticos_ventana)
        self.menu_antibiotico.eliminarAntibioticoBoton.clicked.connect(self.eliminar_antibiotico_ventana)
        self.menu_antibiotico.volverMenuBoton.clicked.connect(lambda: self.volver_menu_principal(self.menu_antibiotico))

        self.agregar_antibiotico.agregarAntibioticoBoton.clicked.connect(self.nuevo_antibiotico)
        self.agregar_antibiotico.volverMenuBoton.clicked.connect(lambda: self.volver_menu_principal(self.agregar_antibiotico))

        self.ver_antibioticos.volverMenuBoton.clicked.connect(lambda: self.volver_menu_principal(self.ver_antibioticos))

        self.eliminar_antibiotico.eliminarProductoBoton.clicked.connect(self.borrar_antibiotico)
        self.eliminar_antibiotico.volverMenuBoton.clicked.connect(lambda: self.volver_menu_principal(self.ver_antibioticos))

    def mostrar_menu_antibiotico(self, menu_principal):
        self.menu_antibiotico.show()
        self.menu_principal = menu_principal

    def agregar_antibiotico_ventana(self):
        self.menu_antibiotico.hide()
        self.agregar_antibiotico.show()

    def ver_antibioticos_ventana(self):
        self.menu_antibiotico.hide()
        self.ver_antibioticos.show()
        todos_antibioticos = main.antibioticos_existentes()  # Supongo que main es una instancia válida aquí
        self.visualizar_antibioticos(todos_antibioticos)

    def eliminar_antibiotico_ventana(self):
        self.menu_antibiotico.hide()
        self.eliminar_antibiotico.show()

    def pop_up(self, mensaje):
        self.pop_up_temp.mensajeRetorno.setText(mensaje)
        self.pop_up_temp.show()
    
    def volver_menu_principal(self, ventana):
        ventana.hide()
        self.menu_principal.show()

    def nuevo_antibiotico(self):
        nombre = self.agregar_antibiotico.nombreAntibioticoInput.text()
        dosis = self.agregar_antibiotico.dosisAntibioticoInput.text()
        tipo_animal = self.agregar_antibiotico.tipoAnimalElegido.currentText()
        valor_producto = self.agregar_antibiotico.valorAntibioticoInput.text()
        mensaje_retorno = main.nuevo_antibiotico(nombre, dosis, tipo_animal, valor_producto)
        self.pop_up(mensaje_retorno)
        self.volver_menu_principal(self.agregar_antibiotico)

    def visualizar_antibioticos(self, lista_antibioticos):
        for antibiotico in lista_antibioticos:
            self.ver_antibioticos.listWidget.addItem(f"{antibiotico.nombre_producto} -- {antibiotico.dosis_antibiotico} -- {antibiotico.tipo_animal} -- {antibiotico.valor_producto}")

    def borrar_antibiotico(self):
        nombre = self.eliminar_antibiotico.cedulaClienteInput.text()
        mensaje_retorno = main.borrar_antibiotico(nombre)
        self.pop_up(mensaje_retorno)
        self.volver_menu_principal(self.eliminar_antibiotico)
