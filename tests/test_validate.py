import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

import validate

def setup_function():
    validate.ids_registrados.clear()

def test_validar_id_valido():
    assert validate.validar_id("P001") is True

def test_validar_id_duplicado():
    validate.ids_registrados.add("P001")
    assert validate.validar_id("P001") is False

def test_validar_id_vacio():
    assert validate.validar_id("") is False

def test_validar_nombre_valido():
    assert validate.validar_nombre("Arroz") is True

def test_validar_nombre_vacio():
    assert validate.validar_nombre("") is False

def test_validar_nombre_muy_corto():
    assert validate.validar_nombre("A") is False

def test_validar_precio_valido():
    assert validate.validar_precio(3500.0) is True

def test_validar_precio_negativo():
    assert validate.validar_precio(-100) is False

def test_validar_precio_cero():
    assert validate.validar_precio(0) is False

def test_validar_precio_texto():
    assert validate.validar_precio("abc") is False

def test_validar_cantidad_valida():
    assert validate.validar_cantidad(10) is True

def test_validar_cantidad_cero():
    assert validate.validar_cantidad(0) is True

def test_validar_cantidad_negativa():
    assert validate.validar_cantidad(-1) is False

def test_validar_categoria_valida():
    assert validate.validar_categoria("alimentos") is True

def test_validar_categoria_invalida():
    assert validate.validar_categoria("comida") is False