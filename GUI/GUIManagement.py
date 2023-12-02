import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5  import  QtWidgets
app = QtWidgets.QApplication([])

from GUI import GUImenuPrincipal as menu


menu.iniciar_main(app)