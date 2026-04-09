# Ejercicio 3 — Menú con múltiples excepciones

def menu():
    while True:
        print("\n--- Menú ---")
        print("1. Dividir números")
        print("2. Abrir archivo y ver primera línea")
        print("3. Salir")

        opcion = input("Elige una opción: ").strip()

        try:
            if opcion == "1":
                a = int(input("  Numerador: "))
                b = int(input("  Denominador: "))
                print(f"  Resultado: {a / b}")

            elif opcion == "2":
                ruta = input("  Ruta del archivo: ").strip()
                with open(ruta, "r", encoding="utf-8") as f:
                    print(f"  Primera línea: {f.readline().rstrip()}")

            elif opcion == "3":
                print("Hasta luego.")
                break

            else:
                print("Opción no válida. Elige 1, 2 o 3.")

        except ValueError:
            print("  ✗ Error: debes ingresar números enteros.")
        except ZeroDivisionError:
            print("  ✗ Error: no se puede dividir entre cero.")
        except FileNotFoundError:
            print("  ✗ Error: archivo no encontrado.")
        except Exception as e:
            print(f"  ✗ Error inesperado: {e}")

menu()