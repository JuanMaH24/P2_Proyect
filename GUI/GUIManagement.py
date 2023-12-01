from PyQt5  import  QtWidgets, uic
app = QtWidgets.QApplication([])

main = uic.loadUi("GUI/Qt_menuprincipal.ui")


def main_categorias():
    id = main.lineEdit.text()
    name = main.lineEdit_2.text()
    lastname = main.lineEdit_4.text()
    tel = main.lineEdit_3.text()
    mail = main.lineEdit_5.text()
    if id and name and lastname and tel and mail:
        succes.label.setText("Productor Agregado!!!")
        succes_window()
    else:
        fail.label.setText("Error al Agregar Productor!!!")
        fail_window()

def main_connect_farm():
    cultive = main.comboBox.currentText()
    locate = main.lineEdit_6.text()
    castral = main.lineEdit_7.text()
    if cultive and locate and castral:
        succes.label.setText("Finca Agregada!!!")
        succes_window()
        main.comboBox.setCurrentIndex(-1)
        main.lineEdit_6.setText("")
        main.lineEdit_7.setText("")
    else:
        fail.label.setText("Error al Agregar Finca!!!")
        fail_window()

def succes_window():
    fail.hide()
    succes.show()

def succes_window_hide():
    succes.hide()


def fail_window():
    succes.hide()
    fail.show()
def fail_window_hide():
    fail.hide()

main.pushButton.clicked.connect(main_connect_user)
main.pushButton_2.clicked.connect(main_connect_farm)
fail.pushButton.clicked.connect(fail_window_hide)
fail.pushButton_2.clicked.connect(fail_window_hide)
succes.pushButton.clicked.connect(succes_window_hide)
succes.pushButton_2.clicked.connect(succes_window_hide)
main.show()
app.exec()