"""
Ejercicio 5: Validador de contraseñas refactorizado
====================================================
Reglas:
  1. Longitud mínima de 8 caracteres
  2. Al menos un dígito
  3. Al menos una letra mayúscula
  4. No puede contener espacios
"""


def is_valid_password(password: str) -> bool:
    """
    Valida si una contraseña cumple con los requisitos de seguridad.

    Args:
        password: La contraseña a validar.

    Returns:
        True si la contraseña es válida, False en caso contrario.
    """
    if len(password) < 8:
        return False

    if " " in password:
        return False

    if not any(char.isdigit() for char in password):
        return False

    if not any(char.isupper() for char in password):
        return False

    return True


# ---------------------------------------------------------------------------
# Pruebas
# ---------------------------------------------------------------------------

def run_tests():
    test_cases = [
        # (contraseña, esperado, descripción)
        ("Abcdefg1",  True,  "válida: mayúscula + dígito + 8 chars"),
        ("abcdefg1",  False, "sin mayúscula"),
        ("ABCDEFGH",  False, "sin dígito"),
        ("Ab1 defg",  False, "contiene espacio"),
        ("Ab1defg",   False, "solo 7 caracteres (< 8)"),
        ("Ab1defgh",  True,  "exactamente 8 caracteres válidos"),
        ("",          False, "cadena vacía"),
        ("A1bcDefgh", True,  "válida: múltiples mayúsculas y dígitos"),
    ]

    passed = 0
    failed = 0

    print("=" * 55)
    print("  PRUEBAS — is_valid_password")
    print("=" * 55)

    for password, expected, description in test_cases:
        result = is_valid_password(password)
        status = " PASS" if result == expected else " FAIL"
        if result == expected:
            passed += 1
        else:
            failed += 1
        print(f"{status}  {repr(password):<14} → {str(result):<5}  ({description})")

    print("-" * 55)
    print(f"  Resultado: {passed} pasaron, {failed} fallaron")
    print("=" * 55)


if __name__ == "__main__":
    run_tests()