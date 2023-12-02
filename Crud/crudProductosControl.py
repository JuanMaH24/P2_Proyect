import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from Modelo.ControlFertilizantes import ControlFertilizantes
from Modelo.ControlesPlagas import ControlesPlagas
from Crud.ICrud import ICrud

class CrudProductosControl(ICrud):

    def __init__(self):
        self.productos_control = []

    def create_control_fertilizante(self, **kwargs):
        try:
            nuevo_producto_control = ControlFertilizantes(**kwargs)
            self.productos_control.append(nuevo_producto_control)
            mensaje = "Fertilizante creado exitosamente"
            return {"Mensaje": mensaje, "Producto_control": nuevo_producto_control}
        except ValueError as error:
            mensaje = str("No se pudo crear el producto")
            return {"Mensaje": mensaje, "Producto_control": None}
    
    def create_control_plagas(self, **kwargs):
        try:
            nuevo_producto_control = ControlesPlagas(**kwargs)
            self.productos_control.append(nuevo_producto_control)
            mensaje = "Control de Plagas creado exitosamente"
            return {"Mensaje": mensaje, "Producto_control": nuevo_producto_control}
        except ValueError as error:
            mensaje = str("No se pudo crear el producto:")
            return {"Mensaje": mensaje, "Producto_control": None}

    def read_productos_control(self):
        productos_control = self.productos_control
        return productos_control
    
    def buscar_producto_control(self, registro_ICA = None):
        registro_ICA = registro_ICA.upper() if registro_ICA else None
        for producto_control in self.productos_control:
            if str(registro_ICA).upper() == str(producto_control.registro_ICA).upper():
                mensaje = "Producto de Control encontrado"
                return {"Mensaje": mensaje, "Producto_control": producto_control}
            
        mensaje = "No se encontró el Producto de Control"
        return {"Mensaje": mensaje, "Producto_control": None}
    

    def update_producto_control(self, registro_ICA = None, nombre_producto = None, frecuencia_aplicacion = None, valor_producto = None, dato_control_plagas_o_fertilizante = None):
        producto_control = self.buscar_producto_control(registro_ICA)
        if producto_control["Producto_control"] != None:
            producto_control["Producto_control"].nombre_producto = nombre_producto
            producto_control["Producto_control"].frecuencia_aplicacion = frecuencia_aplicacion
            producto_control["Producto_control"].valor_producto = valor_producto
            try:
                producto_control["Producto_control"].periodo_carencia = dato_control_plagas_o_fertilizante
            except:
                producto_control["Producto_control"].ultima_aplicacion = dato_control_plagas_o_fertilizante
            mensaje = "Producto de control actualizado correctamente"
            return {"Mensaje": mensaje, "Producto_control": producto_control["Producto_control"]}
        else:
            mensaje = "Producto de control no encontrado"
            return {"Mensaje": mensaje, "Producto_control": None}
        
    # def update_control_plaga(self, registro_ICA = None, nombre_producto = None, frecuencia_aplicacion = None, valor_producto = None, ultima_aplicacion = None):
    #     control_plaga = self.buscar_producto_control(registro_ICA)
    #     if control_plaga["Producto_control"] != None:
    #         control_plaga["Producto_control"].nombre_producto = nombre_producto
    #         control_plaga["Producto_control"].frecuencia_aplicacion = frecuencia_aplicacion
    #         control_plaga["Producto_control"].valor_producto = valor_producto
    #         control_plaga["Producto_control"].ultima_aplicacion = ultima_aplicacion
            
    #         mensaje = "Fertilizante actualizado correctamente"
    #         return {"Mensaje": mensaje, "Producto_control": control_plaga["Producto_control"]}
    #     else:
    #         mensaje = "Fertilizante no encontrado"
    #         return {"Mensaje": mensaje, "Producto_control": None}
        
    def delete_producto_control(self, registro_ICA = None):
        producto_control = self.buscar_producto_control(registro_ICA)
        if producto_control["Producto_control"] != None:
            self.productos_control.remove(producto_control["Producto_control"])
            mensaje= "Se eliminó correctamente el cliente"
            return {"Mensaje": mensaje, "Producto_control": producto_control["Producto_control"]}
        else:
            mensaje= "No se encontró al cliente"
            return {"Mensaje": mensaje, "Producto_control": None}
        
        
    

