from validate import validar_producto, ids_registrados
from file import load_data, save_data

productos: list[dict] = []

def new_register(id: str, nombre: str, precio: float, cantidad: int, categoria: str) -> dict | None:
    if not validar_producto(id=id, nombre=nombre, precio=precio, cantidad=cantidad, categoria=categoria):
        return None

    producto = {
        "id":        id.strip(),
        "nombre":    nombre.strip(),
        "precio":    float(precio),
        "cantidad":  int(cantidad),
        "categoria": categoria.strip().lower(),
    }
    productos.append(producto)
    ids_registrados.add(id.strip())
    save_data(productos)
    return producto

def list_records(orden: str = None) -> list[dict]:
    if orden == "precio":
        return sorted(productos, key=lambda p: p["precio"])
    if orden == "nombre":
        return sorted(productos, key=lambda p: p["nombre"].lower())
    return productos

def search_record(id: str = None, nombre: str = None) -> list[dict]:
    if id:
        return [p for p in productos if p["id"] == id.strip()]
    if nombre:
        return [p for p in productos if nombre.strip().lower() in p["nombre"].lower()]
    return []

def update_record(id: str, **campos) -> bool:
    resultado = [p for p in productos if p["id"] == id.strip()]
    if not resultado:
        print(f"   Producto con ID '{id}' no encontrado.")
        return False

    producto = resultado[0]
    campos_validos = {k: v for k, v in campos.items() if k in ("nombre", "precio", "cantidad", "categoria")}

    for campo, valor in campos_validos.items():
        if not validar_producto(**{campo: valor}):
            return False
        if campo == "precio":
            producto[campo] = float(valor)
        elif campo == "cantidad":
            producto[campo] = int(valor)
        elif campo == "categoria":
            producto[campo] = valor.strip().lower()
        else:
            producto[campo] = valor.strip()

    save_data(productos)
    return True

def delete_record(id: str) -> bool:
    resultado = [p for p in productos if p["id"] == id.strip()]
    if not resultado:
        print(f"   Producto con ID '{id}' no encontrado.")
        return False

    productos.remove(resultado[0])
    ids_registrados.discard(id.strip())
    save_data(productos)
    return True

def cargar_desde_archivo() -> None:
    global productos
    datos = load_data()
    productos.clear()
    for p in datos:
        productos.append(p)
        ids_registrados.add(p["id"])