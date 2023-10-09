import pytest
from Modelo.Clientes import Clientes 
from Modelo.Pedidos import Pedidos
from Modelo.ControlesPlagas import ControlesPlagas
from Modelo.ControlFertilizantes import ControlFertilizantes
from Modelo.Antibioticos import Antibioticos


class Test_relacion_clientes_pedidos:
    @pytest.fixture
    def inicializar (self):
        self.pedido_1 = Pedidos()
        self.pedido_2 = Pedidos()

        self.cliente_1 = Clientes("Sofia Soto", "35892")
        self.producto_plaga_1 = ControlesPlagas("3A5", "Mataa", 12, 1200, "12/11/2022")
        self.producto_plaga_2 = ControlesPlagas("X89", "Maton", 30, 5600, "31/12/2022") 
        self.producto_fertilizante_1= ControlFertilizantes("S3445", "Crecen", 30, 5600, 20)
        self.producto_fertilizante_2= ControlFertilizantes("S3445", "Crecenx2", 23, 11200, 15)
        self.producto_Antibioticos= Antibioticos("Limpia", 500, "Bovino", 220)

    def test_cliente_asociado_pedidos(self,inicializar):
        self.pedido_1.asociar_producto_control(self.producto_fertilizante_1)
        self.pedido_1.asociar_antibiotico(self.producto_Antibioticos)
        self.pedido_2.asociar_producto_control(self.producto_plaga_2)
        self.pedido_2.asociar_producto_control(self.producto_fertilizante_2)

        self.cliente_1.asociar_factura(self.pedido_1)
        self.cliente_1.asociar_factura(self.pedido_2)

        assert  len(self.cliente_1.factura) == 2


if __name__ == "__main__":
    pytest.main()