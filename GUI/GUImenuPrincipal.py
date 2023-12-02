from PyQt5  import  QtWidgets, uic

main = uic.loadUi("GUI/Templates/menu-principal.ui")


def iniciar_main():
    main.show()

def cerrar_main():
    main.hide()
