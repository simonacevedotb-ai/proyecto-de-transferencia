# Ejercicio 1 — Promedio con manejo de errores

def leer_promedio():
    entrada = input("Ingresa enteros separados por comas: ")
    numeros = []

    for parte in entrada.split(","):
        try:
            numeros.append(int(parte.strip()))
        except ValueError:
            print(f"  ⚠ '{parte.strip()}' no es un entero válido, se ignora.")

    if not numeros:
        print("No se ingresaron números válidos.")
        return

    # Bug original: promedio = sum(numeros) / len(entrada)  ← dividía por chars
    promedio = sum(numeros) / len(numeros)
    print(f"Números válidos: {numeros}")
    print(f"Promedio: {promedio:.2f}")

leer_promedio()