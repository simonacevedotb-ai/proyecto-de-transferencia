# Módulo 1 — lógica de negocio (CRUD de productos)
from validate import validar_producto, ids_registrados

productos: list[dict] = []

def crear_producto(id: str, nombre: str, precio: float, cantidad: int, categoria: str) -> dict | None:
    if not validar_producto(id=id, nombre=nombre, precio=precio, cantidad=cantidad, categoria=categoria):
        return None

    producto = {
        "id":       id.strip(),
        "nombre":   nombre.strip(),
        "precio":   float(precio),
        "cantidad": int(cantidad),
        "categoria": categoria.strip().lower(),
    }
    productos.append(producto)
    ids_registrados.add(id.strip())
    return producto

def listar_productos() -> list[dict]:
    return productos

def buscar_producto(id: str) -> dict | None:
    encontrados = [p for p in productos if p["id"] == id.strip()]
    return encontrados[0] if encontrados else None

def actualizar_producto(id: str, **campos) -> bool:
    producto = buscar_producto(id)
    if not producto:
        print(f"  ⚠ Producto con ID '{id}' no encontrado.")
        return False

    campos_validos = {k: v for k, v in campos.items() if k in ("nombre", "precio", "cantidad", "categoria")}
    for campo, valor in campos_validos.items():
        if not validar_producto(**{campo: valor}):
            return False
        producto[campo] = float(valor) if campo == "precio" else (int(valor) if campo == "cantidad" else valor.strip().lower() if campo == "categoria" else valor.strip())
    return True

def eliminar_producto(id: str) -> bool:
    producto = buscar_producto(id)
    if not producto:
        print(f"  ⚠ Producto con ID '{id}' no encontrado.")
        return False
    productos.remove(producto)
    ids_registrados.discard(id.strip())
    return True