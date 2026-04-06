import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from service import crear_producto, listar_productos
from file import load_data, save_data
import validate

if __name__ == "__main__":
    print("Sistema listo\n")

    # Cargar datos desde el archivo
    datos_guardados = load_data()
    for p in datos_guardados:
        validate.ids_registrados.add(p["id"])
        from service import productos
        productos.append(p)

    # Crear productos de prueba solo si el archivo está vacío
    if not listar_productos():
        crear_producto("P001", "Arroz", 3500.0, 50, "alimentos")
        crear_producto("P002", "Shampoo", 12000.0, 20, "limpieza")
        crear_producto("P003", "Audífonos", 85000.0, 5, "electronica")

        # Guardar en el archivo JSON
        save_data(listar_productos())
        print(" Productos guardados en records.json\n")
    else:
        print(" Datos cargados desde records.json\n")

    print("=== Productos en inventario ===")
    for p in listar_productos():
        print(f"  [{p['id']}] {p['nombre']} | ${p['precio']:,.0f} | Stock: {p['cantidad']} | {p['categoria']}")