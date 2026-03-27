import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from service import crear_producto, listar_productos

if __name__ == "__main__":
    print("Sistema listo\n")

    # Datos de prueba M1
    crear_producto("P001", "Arroz", 3500.0, 50, "alimentos")
    crear_producto("P002", "Shampoo", 12000.0, 20, "limpieza")
    crear_producto("P003", "Audífonos", 85000.0, 5, "electronica")

    print("=== Productos en inventario ===")
    for p in listar_productos():
        print(f"  [{p['id']}] {p['nombre']} | ${p['precio']:,.0f} | Stock: {p['cantidad']} | {p['categoria']}")