class Clientes():

  def __init__(self, nombre_cliente, cedula):
    self.__nombre_cliente = nombre_cliente
    self.__cedula= cedula
    self.__factura = []

  @property
  def nombre_cliente(self):
      return self.__nombre_cliente

  @nombre_cliente.setter
  def nombre_cliente(self, nombre_cliente):
    self.__nombre_cliente = nombre_cliente

  @property
  def cedula(self):
      return self.__cedula

  @cedula.setter
  def cedula(self, cedula):
    if not cedula.isdigit():
      raise ValueError("La cédula debe contener solo números.")
    self.__cedula = cedula

  @property
  def factura(self):
      return self.__factura

  @factura.setter
  def factura(self, factura):
    self.__factura.append(factura)

  def asociar_factura(self,factura):
    self.factura.append(factura)