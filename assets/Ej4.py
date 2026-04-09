# Ejercicio 4 — Refactor con excepciones y nombres claros

class OperacionInvalidaError(ValueError):
    """Se lanza cuando la operación solicitada no existe."""

class DivisionPorCeroError(ArithmeticError):
    """Se lanza cuando se intenta dividir entre cero."""


def calcular(a: float, b: float, operacion: str) -> float:
    """
    Realiza la operación entre a y b.
    Operaciones válidas: 'suma', 'resta', 'multi', 'divi'
    Lanza OperacionInvalidaError o DivisionPorCeroError.
    """
    operaciones = {
        "suma":  lambda x, y: x + y,
        "resta": lambda x, y: x - y,
        "multi": lambda x, y: x * y,
        "divi":  lambda x, y: x / y,
    }

    if operacion not in operaciones:
        raise OperacionInvalidaError(
            f"Operación '{operacion}' no reconocida. "
            f"Válidas: {list(operaciones)}"
        )

    if operacion == "divi" and b == 0:
        raise DivisionPorCeroError("El divisor no puede ser cero.")

    return operaciones[operacion](a, b)


# --- Uso con captura de errores ---
try:
    op  = input("Operación (suma, resta, multi, divi): ").strip()
    a   = float(input("Primer número: "))
    b   = float(input("Segundo número: "))
    resultado = calcular(a, b, op)
    print(f"Resultado de {op}: {resultado}")
except OperacionInvalidaError as e:
    print(f"✗ Operación inválida: {e}")
except DivisionPorCeroError as e:
    print(f"✗ División por cero: {e}")
except ValueError:
    print("✗ Los números ingresados no son válidos.")