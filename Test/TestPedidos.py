import pytest
from Modelo import Pedidos 
from Modelo import ControlesPlagas
from Modelo import ControlFertilizantes
from Modelo import Antibioticos


class Test_relacion_pedidos_antibioticos_control:
    @pytest.fixture
    def inicializar(self):
        self.pedido_1 = Pedidos.Pedidos("cualquiera")
        self.producto_plaga_1 = ControlesPlagas.ControlesPlagas("3A5", "Mataa", 12, 1200, "12/11/2022")
        self.producto_plaga_2 = ControlesPlagas.ControlesPlagas("X89", "Maton", 30, 5600, "31/12/2022") 
        self.producto_fertilizante_1= ControlFertilizantes.ControlFertilizantes("S3445", "Crecen", 30, 5600, 20)
        self.producto_fertilizante_2= ControlFertilizantes.ControlFertilizantes("S3445", "Crecenx2", 23, 11200, 15)
        self.producto_Antibioticos= Antibioticos.Antibioticos("Limpia", "10ml", "Bovino", 220)

    def test_pedido_asociado_producto_control(self,inicializar):
        self.pedido_1.asociar_producto_control(self.producto_fertilizante_1)
        self.pedido_1.asociar_producto_control(self.producto_plaga_2)
        self.pedido_1.asociar_producto_control(self.producto_fertilizante_2)

        assert len(self.pedido_1.producto_control) == 3

    def test_pedido_asociado_antibiotico(self,inicializar):
        self.pedido_1.asociar_antibiotico(self.producto_Antibioticos)
        assert len(self.pedido_1.antibiotico) == 1


if __name__ == "__main__":
    pytest.main()
    


    

