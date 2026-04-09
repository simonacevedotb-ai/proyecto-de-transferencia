import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from service import cargar_desde_archivo
from menu import mostrar_menu

if __name__ == "__main__":
    print("Sistema listo")
    cargar_desde_archivo()
    mostrar_menu()