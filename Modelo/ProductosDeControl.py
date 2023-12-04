class ProductosDeControl():

    def __init__(self, registro_ICA, nombre_producto, frecuencia_aplicacion, valor_producto,periodo_carencia):
        if valor_producto < 0:
            raise ValueError("El valor no puede ser negativo.")
        self.__nombre_producto = nombre_producto
        self.__registro_ICA = registro_ICA
        self.__frecuencia_aplicacion = frecuencia_aplicacion
        self.__valor_producto = valor_producto
        self.__periodo_carencia=periodo_carencia

    @property
    def nombre_producto(self):
        return self.__nombre_producto

    @nombre_producto.setter
    def nombre_producto(self, nombre_producto):
        self.__nombre_producto = nombre_producto

    @property
    def registro_ICA(self):
        return self.__registro_ICA

    @registro_ICA.setter
    def registro_ICA(self, registro_ICA):
        self.__registro_ICA = registro_ICA

    @property
    def frecuencia_aplicacion(self):
        return self.__frecuencia_aplicacion

    @frecuencia_aplicacion.setter
    def frecuencia_aplicacion(self, frecuencia_aplicacion):
        self.__frecuencia_aplicacion = frecuencia_aplicacion
    
    @property
    def periodo_carencia(self):
        return self.__periodo_carencia

    @periodo_carencia.setter
    def periodo_carencian(self, periodo_carencia):
        self.__periodo_carencia = periodo_carencia

    @property
    def valor_producto(self):
        return self.__valor_producto

    @valor_producto.setter
    def valor_producto(self, valor_producto):
        if valor_producto < 0:
            raise ValueError("El valor no puede ser negativo.")
        self.__valor_producto = valor_producto
