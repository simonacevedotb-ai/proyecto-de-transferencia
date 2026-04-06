import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from service import new_register, list_records, search_record, update_record, delete_record, cargar_desde_archivo

if __name__ == "__main__":
    print("Sistema listo\n")

    # Cargar datos existentes desde el archivo
    cargar_desde_archivo()

    # --- CREAR ---
    print("=== CREAR ===")
    new_register("P001", "Arroz", 3500.0, 50, "alimentos")
    new_register("P002", "Shampoo", 12000.0, 20, "limpieza")
    new_register("P003", "Audífonos", 85000.0, 5, "electronica")
    new_register("P004", "Coca Cola", 4000.0, 100, "bebidas")
    print(" 4 productos creados y guardados\n")

    # --- LISTAR (ordenado por precio) ---
    print("=== LISTAR (ordenado por precio) ===")
    for p in list_records(orden="precio"):
        print(f"  [{p['id']}] {p['nombre']} | ${p['precio']:,.0f} | Stock: {p['cantidad']} | {p['categoria']}")

    # --- BUSCAR ---
    print("\n=== BUSCAR (nombre contiene 'a') ===")
    resultados = search_record(nombre="a")
    for p in resultados:
        print(f"  [{p['id']}] {p['nombre']}")

    # --- ACTUALIZAR ---
    print("\n=== ACTUALIZAR (P002 precio y cantidad) ===")
    ok = update_record("P002", precio=15000.0, cantidad=30)
    if ok:
        print("   P002 actualizado")

    # --- ELIMINAR ---
    print("\n=== ELIMINAR (P004) ===")
    ok = delete_record("P004")
    if ok:
        print("   P004 eliminado")

    # --- LISTAR FINAL ---
    print("\n=== INVENTARIO FINAL ===")
    for p in list_records(orden="nombre"):
        print(f"  [{p['id']}] {p['nombre']} | ${p['precio']:,.0f} | Stock: {p['cantidad']} | {p['categoria']}")