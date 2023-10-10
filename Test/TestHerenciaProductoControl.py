import pytest
from Modelo.ControlesPlagas import ControlesPlagas
from Modelo.ControlFertilizantes import ControlFertilizantes

class Test_herencia_productos_control:
    @pytest.fixture
    def inicializar(self):
        self.control_plagas = ControlesPlagas("123", "Plaguicida A", "Quincenal", 50.0, 7)
        self.control_fertilizantes = ControlFertilizantes("456", "Fertilizante B", "Mensual", 30.0, "2023-10-10")

    def test_producto_control_plagas(self, inicializar):
        assert self.control_plagas.registro_ICA == "123"
        assert self.control_plagas.nombre_producto == "Plaguicida A"
        assert self.control_plagas.frecuencia_aplicacion == "Quincenal"
        assert self.control_plagas.valor_producto == 50.0
        assert self.control_plagas.ultima_aplicacion == 7
    
    def test_producto_control_fertilizantes(self, inicializar):
        assert self.control_fertilizantes.registro_ICA == "456"
        assert self.control_fertilizantes.nombre_producto == "Fertilizante B"
        assert self.control_fertilizantes.frecuencia_aplicacion == "Mensual"
        assert self.control_fertilizantes.valor_producto == 30.0
        assert self.control_fertilizantes.periodo_carencia ==  "2023-10-10"

if __name__ == "__main__":
    pytest.main()