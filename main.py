import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)
from UI.ui import menu_opciones

def menu():
    menu_opciones(0)
    
menu()