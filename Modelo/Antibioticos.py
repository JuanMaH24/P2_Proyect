class Antibioticos():
  
    def __init__(self, nombre_producto, dosis_antibiotico, tipo_animal, valor_producto):
        if nombre_producto== "" or dosis_antibiotico== "" or tipo_animal== "" or valor_producto== "":
            raise(ValueError("Debes ingresar todos los campos"))
        if dosis_antibiotico >= 400 and dosis_antibiotico >= 600:
            raise (ValueError("La dosis debe estar entre 400 y 600."))
        if tipo_animal.upper() not in ["BOVINO", "PORCINO", "CAPRINO"]:
            raise (ValueError("El tipo de animal no es válido."))
        if valor_producto < 0:
            raise (ValueError("El valor no puede ser negativo."))
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
        if dosis_antibiotico >= 400 and dosis_antibiotico >= 600:
            raise ValueError("La dosis debe estar entre 400 y 600.")
        self.__dosis_antibiotico = dosis_antibiotico

    @property
    def tipo_animal(self):
        return self.__tipo_animal

    @tipo_animal.setter
    def tipo_animal(self, tipo_animal):
        if tipo_animal.upper() not in ["BOVINO", "PORCINO", "CAPRINO"]:
            raise ValueError("El tipo de animal no es válido.")
        self.__tipo_animal = tipo_animal

    @property
    def valor_producto(self):
        return self.__valor_producto

    @valor_producto.setter
    def valor_producto(self, valor_producto):
        if valor_producto < 0:
            raise ValueError("El valor no puede ser negativo.")
        self.__valor_producto = valor_producto
