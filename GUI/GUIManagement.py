from PyQt5  import  QtWidgets, uic
app = QtWidgets.QApplication([])


main = uic.loadUi("GUI/Templates/menu-principal.ui")
menu_clientes = uic.loadUi("GUI/Templates/menu-clientes.ui")
menu_antibiotico = uic.loadUi("GUI/Templates/menu-antibioticos.ui")
menu_productos = uic.loadUi("GUI/Templates/menu-producto-control.ui") 

def volver(ventana):
    ventana.hide()
    main.show()

def start ():
    main.show()
    sys.exit(app.exec_())

def menu_clientes_ventana():
    main.hide()
    menu_clientes.show()

def menu_antibiotico_ventana():
    main.hide()
    menu_antibiotico.show()

def menu_productos_ventana():
    main.hide()
    menu_productos.show()


main.clientesBoton.clicked.connect(menu_clientes_ventana)
main.prodControlBoton.clicked.connect(menu_productos_ventana)
main.antibioticoBoton.clicked.connect(menu_antibiotico_ventana)

if __name__ == '__main__':
    import sys
    start()
    