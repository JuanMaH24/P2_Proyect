import pytest
from Modelo.Antibioticos import Antibioticos


def test_espacios_vacios():
    with pytest.raises(ValueError, match="Debes ingresar todos los campos"):
        Antibioticos("", "", "", "")

def test_dosis_antibioticos():
    with pytest.raises(ValueError, match="La dosis debe estar entre 400 y 600."):
        Antibioticos("AntibioticMAx3", 650, "CAPRINO", 123000)

def test_tipo_animal():
    with pytest.raises(ValueError, match="El tipo de animal no es válido."):
        Antibioticos("AntibioticMAx3", 450, "Caballo", 123000)

def test_valor_negativo():
    with pytest.raises(ValueError, match="El valor no puede ser negativo."):
        Antibioticos("AntibioticMAx3", 450, "Caprino", -124000)