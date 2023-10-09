from Modelo.ProductosDeControl import ProductosDeControl 

class ControlFertilizantes(ProductosDeControl):
    def __init__(self, registro_ICA, nombre_producto, frecuencia_aplicacion, valor_producto, periodo_carencia):
        super().__init__(registro_ICA, nombre_producto, frecuencia_aplicacion, valor_producto)
        self.__periodo_carencia = periodo_carencia
    
    @property
    def periodo_carencia(self):
        return self.__periodo_carencia

    @periodo_carencia.setter
    def periodo_carencia(self, periodo_carencia):
        self.__periodo_carencia = periodo_carencia
    