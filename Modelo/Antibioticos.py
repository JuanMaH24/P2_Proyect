class Antibioticos():
  
    def __init__(self, nombre_producto, dosis_antibiotico, tipo_animal, valor_producto):
        self.__nombre_producto = nombre_producto
        self.__dosis_antibiotico = dosis_antibiotico
        self.__tipo_animal = tipo_animal
        self.__valor_producto = valor_producto

    @property
    def nombre_producto(self):
        return self.__nombre_producto

    @nombre_producto.setter
    def nombre_producto(self, nombre_producto):
        self.__nombre_producto = nombre_producto

    @property
    def dosis_antibiotico(self):
        return self.__dosis_antibiotico

    @dosis_antibiotico.setter
    def dosis_antibiotico(self, dosis_antibiotico):
        self.__dosis_antibiotico = dosis_antibiotico

    @property
    def tipo_animal(self):
        return self.__tipo_animal

    @tipo_animal.setter
    def tipo_animal(self, tipo_animal):
        self.__tipo_animal = tipo_animal

    @property
    def valor_producto(self):
        return self.__valor_producto

    @valor_producto.setter
    def valor_producto(self, valor_producto):
        self.__valor_producto = valor_producto
