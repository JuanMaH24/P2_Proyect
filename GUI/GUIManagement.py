import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5  import  QtWidgets, uic
from GUI.ClientesManagement import ClientesManagement
from GUI.AntibioticosManagement import ManejadorAntibioticos
from GUI.ProductosManagement import ProductosManagement

app = QtWidgets.QApplication([])


menu_cliente = ClientesManagement()
menu_productos = ProductosManagement()
menu_antibiotico = ManejadorAntibioticos()
main = uic.loadUi("GUI/Templates/menu-principal.ui")
# menu_antibiotico = uic.loadUi("GUI/Templates/menu-antibioticos.ui")
# menu_productos = uic.loadUi("GUI/Templates/menu-producto-control.ui") 

def volver(ventana):
    ventana.hide()
    main.show()

def start ():
    main.show()
    sys.exit(app.exec_())

def menu_clientes_ventana():
    main.hide()
    menu_cliente.mostrar_menu_cliente(main)

def menu_antibiotico_ventana():
    main.hide()
    menu_antibiotico.mostrar_menu_antibiotico(main)

def menu_productos_ventana():
    main.hide()
    menu_productos.mostrar_menu_productos(main)


main.clientesBoton.clicked.connect(menu_clientes_ventana)
main.prodControlBoton.clicked.connect(menu_productos_ventana)
main.antibioticoBoton.clicked.connect(menu_antibiotico_ventana)

start()
    