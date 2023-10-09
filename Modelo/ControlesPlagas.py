from Modelo.ProductosDeControl import ProductosDeControl 

class ControlesPlagas(ProductosDeControl):
    def __init__(self, registro_ICA, nombre_producto, frecuencia_aplicacion, valor_producto, ultima_aplicacion):
        super().__init__(registro_ICA, nombre_producto, frecuencia_aplicacion, valor_producto)
        self.__ultima_aplicacion = ultima_aplicacion
    
    @property
    def ultima_aplicacion(self):
        return self.__ultima_aplicacion

    @ultima_aplicacion.setter
    def ultima_aplicacion(self, ultima_aplicacion):
        self.__ultima_aplicacion = ultima_aplicacion
    