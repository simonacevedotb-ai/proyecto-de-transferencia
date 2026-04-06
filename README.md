# Sistema de Gestión de Inventario

Sistema CRUD en consola para gestionar productos, con persistencia en JSON y código modular en Python.

## Requisitos

- Python 3.10+
- Instalar dependencias:

```bash
pip install -r requirements.txt
```

## Cómo ejecutar

```bash
cd src
python main.py
```

## Estructura del proyecto

```
proyecto-de-transferencia/
├── README.md
├── requirements.txt
├── .gitignore
├── data/
│   └── records.json
└── src/
    ├── main.py        # Punto de entrada
    ├── menu.py        # Menú interactivo en consola
    ├── service.py     # Lógica CRUD de productos
    ├── file.py        # Lectura y escritura de archivos
    ├── validate.py    # Validaciones y helpers
    └── integration.py # Integración con faker
```

## Módulos

| Módulo | Tag | Estado |
|---|---|---|
| M0 — Estructura del repositorio | `m0-setup` |  |
| M1 — Estructuras de datos y validaciones | `m1-data` |  |