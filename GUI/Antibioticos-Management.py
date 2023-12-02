from PyQt5  import  QtWidgets, uic
import main 
from GUI import GUIManagement
app = QtWidgets.QApplication([])


menu_antibiotico = uic.loadUi("GUI/Templates/menu-antibioticos.ui")
agregar_antibiotico = uic.loadUi("GUI/Templates/agregar-antibiotico.ui")
ver_antibioticos = uic.loadUi("GUI/Templates/ver-antibioticos.ui")
eliminar_antibiotico = uic.loadUi("GUI/Templates/eliminar-antibiotico.ui")
pop_up_temp = uic.loadUi("GUI/Templates/pop-up.ui")    


def agregar_antibiotico_ventana():
    menu_antibiotico.hide()
    agregar_antibiotico.show()

def ver_antibioticos_ventana():
    menu_antibiotico.hide()
    ver_antibioticos.show()
    todos_antibioticos = main.antibioticos_existentes()
    visualizar_antibioticos(todos_antibioticos)

def eliminar_antibiotico_ventana():
    menu_antibiotico.hide()
    eliminar_antibiotico.show()

def pop_up(mensaje):
    pop_up_temp.mensajeRetorno.setText(mensaje)
    pop_up_temp.show()

def volver_menu_principal(ventana):
    GUIManagement.volver(ventana)

menu_antibiotico.nuevoAntibioticoBoton.clicked.connect(agregar_antibiotico_ventana)
menu_antibiotico.verAntibioticosBoton.clicked.connect(ver_antibioticos_ventana)
menu_antibiotico.eliminarAntibioticoBoton.clicked.connect(eliminar_antibiotico_ventana)
menu_antibiotico.volverMenuBoton.clicked.connect(volver_menu_principal(menu_antibiotico))

def nuevo_antibiotico():
    nombre = agregar_antibiotico.nombreAntibioticoInput.text()
    dosis =  agregar_antibiotico.dosisAntibioticoInput.text()
    tipo_animal =  agregar_antibiotico.tipoAnimalElegido.currentText()
    valor_producto = agregar_antibiotico.valorAntibioticoInput.text()
    mensaje_retorno = main.nuevo_antibiotico(nombre, dosis, tipo_animal, valor_producto)
    pop_up(mensaje_retorno)
    volver_menu_principal(agregar_antibiotico)

agregar_antibiotico.agregarAntibioticoBoton.clicked.connect(nuevo_antibiotico)
agregar_antibiotico.volverMenuBoton.clicked.connect(volver_menu_principal(agregar_antibiotico))

def visualizar_antibioticos(lista_antibioticos):
    for antibiotico in lista_antibioticos:
        ver_antibioticos.listWidget.addItem(f"{antibiotico.nombre_producto} -- {antibiotico.dosis_antibiotico} -- {antibiotico.tipo_animal} -- {antibiotico.valor_producto}")

ver_antibioticos.volverMenuBoton.clicked.connect(volver_menu_principal(ver_antibioticos))

def borrar_antibiotico():
    nombre= eliminar_antibiotico.cedulaClienteInput.text()
    mensaje_retorno = main.borrar_antibiotico(nombre)
    pop_up(mensaje_retorno)
    volver_menu_principal(eliminar_antibiotico)

eliminar_antibiotico.eliminarProductoBoton.clicked.connect(borrar_antibiotico)
ver_antibioticos.volverMenuBoton.clicked.connect(volver_menu_principal(ver_antibioticos))