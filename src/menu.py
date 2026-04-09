from colorama import init, Fore, Style
from service import new_register, list_records, search_record, update_record, delete_record

init(autoreset=True)

def titulo(texto: str) -> None:
    print(f"\n{Fore.CYAN}{'='*45}")
    print(f"  {texto}")
    print(f"{'='*45}{Style.RESET_ALL}")

def exito(texto: str) -> None:
    print(f"{Fore.GREEN}   {texto}{Style.RESET_ALL}")

def error(texto: str) -> None:
    print(f"{Fore.RED}   {texto}{Style.RESET_ALL}")

def advertencia(texto: str) -> None:
    print(f"{Fore.YELLOW}  ⚠ {texto}{Style.RESET_ALL}")

def pedir_input(etiqueta: str) -> str:
    return input(f"{Fore.WHITE}  {etiqueta}: {Style.RESET_ALL}").strip()

def mostrar_producto(p: dict) -> None:
    print(f"  {Fore.CYAN}[{p['id']}]{Style.RESET_ALL} {p['nombre']} | "
        f"{Fore.GREEN}${p['precio']:,.0f}{Style.RESET_ALL} | "
        f"Stock: {p['cantidad']} | {Fore.YELLOW}{p['categoria']}{Style.RESET_ALL}")

# ── Opciones del menú ──────────────────────────────────────

def opcion_crear():
    titulo("CREAR PRODUCTO")
    try:
        id        = pedir_input("ID (ej: P010)")
        nombre    = pedir_input("Nombre")
        precio    = pedir_input("Precio")
        cantidad  = pedir_input("Cantidad")
        categoria = pedir_input("Categoría (alimentos/bebidas/limpieza/electronica/ropa/otro)")

        resultado = new_register(id, nombre, precio, cantidad, categoria)
        if resultado:
            exito(f"Producto '{resultado['nombre']}' creado correctamente.")
    except Exception as e:
        error(f"Error inesperado: {e}")

def opcion_listar():
    titulo("LISTAR PRODUCTOS")
    print(f"  Ordenar por: {Fore.CYAN}1{Style.RESET_ALL}) Precio  "
        f"{Fore.CYAN}2{Style.RESET_ALL}) Nombre  "
        f"{Fore.CYAN}3{Style.RESET_ALL}) Sin orden")
    opcion = pedir_input("Opción")
    orden = {"1": "precio", "2": "nombre"}.get(opcion, None)
    productos = list_records(orden=orden)
    if not productos:
        advertencia("No hay productos registrados.")
        return
    for p in productos:
        mostrar_producto(p)

def opcion_buscar():
    titulo("BUSCAR PRODUCTO")
    print(f"  Buscar por: {Fore.CYAN}1{Style.RESET_ALL}) ID  {Fore.CYAN}2{Style.RESET_ALL}) Nombre")
    opcion = pedir_input("Opción")
    try:
        if opcion == "1":
            id = pedir_input("ID")
            resultados = search_record(id=id)
        elif opcion == "2":
            nombre = pedir_input("Nombre (parcial)")
            resultados = search_record(nombre=nombre)
        else:
            advertencia("Opción no válida.")
            return

        if not resultados:
            advertencia("No se encontraron productos.")
        else:
            for p in resultados:
                mostrar_producto(p)
    except Exception as e:
        error(f"Error inesperado: {e}")

def opcion_actualizar():
    titulo("ACTUALIZAR PRODUCTO")
    try:
        id = pedir_input("ID del producto a actualizar")
        print("  Deja en blanco los campos que no quieras cambiar.")
        nombre    = pedir_input("Nuevo nombre")
        precio    = pedir_input("Nuevo precio")
        cantidad  = pedir_input("Nueva cantidad")
        categoria = pedir_input("Nueva categoría")

        campos = {}
        if nombre:    campos["nombre"]    = nombre
        if precio:    campos["precio"]    = precio
        if cantidad:  campos["cantidad"]  = cantidad
        if categoria: campos["categoria"] = categoria

        if not campos:
            advertencia("No ingresaste ningún campo para actualizar.")
            return

        ok = update_record(id, **campos)
        if ok:
            exito("Producto actualizado correctamente.")
    except Exception as e:
        error(f"Error inesperado: {e}")

def opcion_eliminar():
    titulo("ELIMINAR PRODUCTO")
    try:
        id = pedir_input("ID del producto a eliminar")
        confirmacion = pedir_input(f"¿Seguro que quieres eliminar '{id}'? (s/n)")
        if confirmacion.lower() != "s":
            advertencia("Operación cancelada.")
            return
        ok = delete_record(id)
        if ok:
            exito(f"Producto '{id}' eliminado correctamente.")
    except Exception as e:
        error(f"Error inesperado: {e}")

# ── Menú principal ─────────────────────────────────────────

def mostrar_menu():
    opciones = {
        "1": ("Crear producto",      opcion_crear),
        "2": ("Listar productos",    opcion_listar),
        "3": ("Buscar producto",     opcion_buscar),
        "4": ("Actualizar producto", opcion_actualizar),
        "5": ("Eliminar producto",   opcion_eliminar),
        "6": ("Salir",               None),
    }

    while True:
        titulo("SISTEMA DE GESTIÓN DE INVENTARIO")
        for clave, (descripcion, _) in opciones.items():
            color = Fore.RED if clave == "6" else Fore.CYAN
            print(f"  {color}[{clave}]{Style.RESET_ALL} {descripcion}")

        opcion = pedir_input("\nElige una opción")

        if opcion == "6":
            print(f"\n{Fore.YELLOW}  Hasta luego {Style.RESET_ALL}\n")
            break
        elif opcion in opciones:
            opciones[opcion][1]()
        else:
            error("Opción no válida. Elige entre 1 y 6.")