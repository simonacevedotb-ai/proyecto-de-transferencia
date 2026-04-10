import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

import validate
from service import new_register, list_records, search_record, update_record, delete_record, productos

def setup_function():
    productos.clear()
    validate.ids_registrados.clear()

def test_crear_producto_valido():
    p = new_register("P001", "Arroz", 3500.0, 50, "alimentos")
    assert p is not None
    assert p["id"] == "P001"
    assert p["nombre"] == "Arroz"
    assert p["precio"] == 3500.0

def test_crear_producto_id_duplicado():
    new_register("P001", "Arroz", 3500.0, 50, "alimentos")
    p = new_register("P001", "Leche", 2000.0, 10, "bebidas")
    assert p is None

def test_crear_producto_precio_invalido():
    p = new_register("P002", "Leche", -100.0, 10, "bebidas")
    assert p is None

def test_crear_producto_cantidad_negativa():
    p = new_register("P003", "Pan", 1500.0, -5, "alimentos")
    assert p is None

def test_listar_productos_ordenado_por_precio():
    new_register("P001", "Audífonos", 85000.0, 5, "electronica")
    new_register("P002", "Arroz", 3500.0, 50, "alimentos")
    new_register("P003", "Shampoo", 12000.0, 20, "limpieza")
    resultado = list_records(orden="precio")
    precios = [p["precio"] for p in resultado]
    assert precios == sorted(precios)

def test_buscar_producto_por_id():
    new_register("P001", "Arroz", 3500.0, 50, "alimentos")
    resultado = search_record(id="P001")
    assert len(resultado) == 1
    assert resultado[0]["nombre"] == "Arroz"

def test_buscar_producto_inexistente():
    resultado = search_record(id="X999")
    assert resultado == []

def test_buscar_producto_por_nombre_parcial():
    new_register("P001", "Arroz", 3500.0, 50, "alimentos")
    new_register("P002", "Arándano", 8000.0, 15, "alimentos")
    resultado = search_record(nombre="ar")
    assert len(resultado) == 2

def test_actualizar_producto():
    new_register("P001", "Arroz", 3500.0, 50, "alimentos")
    ok = update_record("P001", precio=4000.0, cantidad=60)
    assert ok is True
    p = search_record(id="P001")[0]
    assert p["precio"] == 4000.0
    assert p["cantidad"] == 60

def test_actualizar_producto_inexistente():
    ok = update_record("X999", precio=1000.0)
    assert ok is False

def test_eliminar_producto():
    new_register("P001", "Arroz", 3500.0, 50, "alimentos")
    ok = delete_record("P001")
    assert ok is True
    assert search_record(id="P001") == []

def test_eliminar_producto_inexistente():
    ok = delete_record("X999")
    assert ok is False