# Módulo de validaciones y helpers
ids_registrados = set()

def validar_id(id_producto: str) -> bool:
    if not id_producto or not id_producto.strip():
        print("   El ID no puede estar vacío.")
        return False
    if id_producto in ids_registrados:
        print(f"   El ID '{id_producto}' ya existe.")
        return False
    return True

def validar_nombre(nombre: str) -> bool:
    if not nombre or not nombre.strip():
        print("   El nombre no puede estar vacío.")
        return False
    if len(nombre.strip()) < 2:
        print("   El nombre debe tener al menos 2 caracteres.")
        return False
    return True

def validar_precio(precio) -> bool:
    try:
        valor = float(precio)
        if valor <= 0:
            print("   El precio debe ser mayor a 0.")
            return False
        return True
    except (ValueError, TypeError):
        print("   El precio debe ser un número válido.")
        return False

def validar_cantidad(cantidad) -> bool:
    try:
        valor = int(cantidad)
        if valor < 0:
            print("   La cantidad no puede ser negativa.")
            return False
        return True
    except (ValueError, TypeError):
        print("   La cantidad debe ser un número entero.")
        return False

def validar_categoria(categoria: str) -> bool:
    categorias_validas = {"alimentos", "bebidas", "limpieza", "electronica", "ropa", "otro"}
    if categoria.strip().lower() not in categorias_validas:
        print(f"   Categoría inválida. Válidas: {categorias_validas}")
        return False
    return True

def validar_producto(**kwargs) -> bool:
    validaciones = {
        "id":        lambda v: validar_id(v),
        "nombre":    lambda v: validar_nombre(v),
        "precio":    lambda v: validar_precio(v),
        "cantidad":  lambda v: validar_cantidad(v),
        "categoria": lambda v: validar_categoria(v),
    }
    for campo, valor in kwargs.items():
        if campo in validaciones:
            if not validaciones[campo](valor):
                return False
    return True