# Ejercicio 2 — Archivo con try/except/else/finally

def contar_lineas(ruta: str):
    archivo = None
    try:
        archivo = open(ruta, "r", encoding="utf-8")
    except FileNotFoundError:
        print(f"Error: el archivo '{ruta}' no existe.")
    except PermissionError:
        print(f"Error: sin permisos para leer '{ruta}'.")
    else:
        # Solo se ejecuta si open() tuvo éxito (sin excepción)
        lineas = archivo.readlines()
        print(f"El archivo tiene {len(lineas)} líneas.")
    finally:
        # Siempre se ejecuta: con o sin error
        if archivo:
            archivo.close()
        print("Operación finalizada.")

contar_lineas("datos.txt")