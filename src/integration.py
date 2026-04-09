from faker import Faker
import random
from service import new_register

fake = Faker("es_ES")

CATEGORIAS = ["alimentos", "bebidas", "limpieza", "electronica", "ropa", "otro"]

def generar_producto_falso() -> dict:
    return {
        "id":        f"F{random.randint(100, 999)}",
        "nombre":    fake.word().capitalize(),
        "precio":    round(random.uniform(1000, 150000), 0),
        "cantidad":  random.randint(1, 100),
        "categoria": random.choice(CATEGORIAS),
    }

def cargar_productos_faker(cantidad: int = 5) -> list[dict]:
    creados = []
    intentos = 0

    while len(creados) < cantidad and intentos < cantidad * 3:
        p = generar_producto_falso()
        resultado = new_register(p["id"], p["nombre"], p["precio"], p["cantidad"], p["categoria"])
        if resultado:
            creados.append(resultado)
        intentos += 1

    return creados