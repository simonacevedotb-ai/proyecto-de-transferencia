import json
import os

RUTA_ARCHIVO = os.path.join(os.path.dirname(__file__), "..", "data", "records.json")

def load_data() -> list[dict]:
    try:
        with open(RUTA_ARCHIVO, "r", encoding="utf-8") as f:
            datos = json.load(f)
            return datos
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("  ⚠ El archivo de datos está dañado. Se arranca con lista vacía.")
        return []
    except Exception as e:
        print(f"  ⚠ Error inesperado al leer el archivo: {e}")
        return []

def save_data(data: list[dict]) -> bool:
    try:
        os.makedirs(os.path.dirname(RUTA_ARCHIVO), exist_ok=True)
        with open(RUTA_ARCHIVO, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return True
    except PermissionError:
        print("  ⚠ Sin permisos para escribir el archivo.")
        return False
    except Exception as e:
        print(f"  ⚠ Error inesperado al guardar: {e}")
        return False