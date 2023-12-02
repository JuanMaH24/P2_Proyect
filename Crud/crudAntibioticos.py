import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from Modelo.Antibioticos import Antibioticos
from Crud.ICrud import ICrud


class CrudAntibiotico(ICrud):

    def __init__(self):
        self.antibioticos = []
    

    def create_antibiotico(self,**kwargs):
        try:
            nuevo_antibiotico = Antibioticos(**kwargs)
            self.antibioticos.append(nuevo_antibiotico)
            mensaje = "Antibiotico creado exitosamente"
            return {"Mensaje": mensaje, "Antibiotico": nuevo_antibiotico}
        except ValueError as error:
            mensaje = str("No se pudo crear el nuevo antibiotico: ")
            return {"Mensaje": mensaje, "Antibiotico": None}

    def read(self):
        Antibioticos = self.antibioticos
        return Antibioticos
    

    def buscar_antibioticos(self, nombre_producto=None):
        nombre_producto = nombre_producto.upper() if nombre_producto else None
        for antibiotico in self.antibioticos:
            if nombre_producto == antibiotico.nombre_producto.upper():
                mensaje = "Antibiotico encontrado"
                return {"Mensaje": mensaje, "Antibiotico": antibiotico}
            
        mensaje = "No se encontró el antibiotico"
        return {"Mensaje": mensaje, "Antibiotico": None}

    #Agregar facturas a un cliente ya creado
    def update_antibiotico(self, nombre_producto=None, **kwargs):
        antibiotico = self.buscar(nombre_producto)
        if antibiotico["Antibiotico"] is not None:
            for key, value in kwargs.items():
                setattr(antibiotico["Antibiotico"], key, value)
            mensaje = "Se actualizó correctamente el antibiotico"
            return {"Mensaje": mensaje, "Antibiotico": antibiotico["Antibiotico"]}
        else:
            mensaje = "No se encontró el antibiotico"
            return {"Mensaje": mensaje, "Antibiotico": None}
    
    def delete_antibiotico(self, nombre_producto=None):
        antibiotico = self.buscar_antibioticos(nombre_producto)
        if antibiotico["Antibiotico"] != None:
            self.antibioticos.remove(antibiotico["Antibiotico"])
            mensaje= "Se eliminó correctamente el antibiotico"
            return {"Mensaje": mensaje, "Antibiotico": antibiotico["Antibiotico"]}
        else:
            mensaje= "No se encontró el antibiotico"
            return {"Mensaje": mensaje, "Antibiotico": None}


















