import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from Modelo.Antibioticos import Antibioticos


class CrudAntibiotico():
    def __init__(self):
        self.antibioticos = []
    

    def create_antibiotico(self,nombre_producto=None, dosis_antibiotico=None, tipo_animal=None, valor_producto=None):
        try:
            nuevo_antibiotico= Antibioticos(nombre_producto,dosis_antibiotico,tipo_animal,valor_producto)
            self.antibioticos.append(nuevo_antibiotico)
            mensaje = "Antibiotico creado exitosamente"
            return {"Mensaje": mensaje, "Antibiotico": nuevo_antibiotico}
        except ValueError as error:
            mensaje = str("No se pudo crear el nuevo antibiotico: ")
            return {"Mensaje": mensaje, "Antibiotico": None}
        
    def read(self):
        Antibioticos = self.antibioticos
        return Antibioticos
    
    def buscar_antibioticos(self,nombre_producto=None):
        for antibiotico in self.antibioticos:
            if nombre_producto.upper() == antibiotico.nombre_producto.upper():
                mensaje = "Antibiotico encontrado"
                return {"Mensaje": mensaje, "Antibiotico": antibiotico}
            
        mensaje= "No se encontró el antibiotico"
        return {"Mensaje": mensaje, "Antibiotico": None}
    
    #Agregar facturas a un cliente ya creado
    def update_antibiotico(self, nombre_producto=None, dosis_antibiotico=None, tipo_animal=None, valor_producto=None):
        antibiotico = self.buscar_antibioticos(nombre_producto)
        if antibiotico["Antibiotico"] != None:
            antibiotico["Antibiotico"].nombre_producto = nombre_producto
            antibiotico["Antibiotico"].dosis_antibiotico = dosis_antibiotico
            antibiotico["Antibiotico"].tipo_animal = tipo_animal
            antibiotico["Antibiotico"].valor_producto =  valor_producto
            mensaje= "Se actualizó correctamente el antibiotico"
            return {"Mensaje": mensaje, "Antibiotico": antibiotico["Antibiotico"]}
        else:
            mensaje= "No se encontró el antiobiotico"
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



















