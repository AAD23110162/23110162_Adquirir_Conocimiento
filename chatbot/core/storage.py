import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
CLIENTES_FILE = DATA_DIR / "clientes.json"
MARCA_FILE = DATA_DIR / "marca.json"


def _cargar_json(path: Path, datos_por_defecto: dict) -> dict:
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    if not path.exists():
        _guardar_json(path, datos_por_defecto)
        return datos_por_defecto.copy()

    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def _guardar_json(path: Path, datos: dict) -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as file:
        json.dump(datos, file, ensure_ascii=False, indent=2)


def cargar_clientes() -> dict:
    datos_base = {
        "clientes": {
            "1234": {
                "nombre": "Juan Perez",
                "proyectos": {
                    "pagina web": "En desarrollo (50%)",
                    "sistema de inventario": "Finalizado"
                },
                "cotizaciones": []
            }
        }
    }
    return _cargar_json(CLIENTES_FILE, datos_base)


def guardar_clientes(datos_clientes: dict) -> None:
    _guardar_json(CLIENTES_FILE, datos_clientes)


def cargar_marca() -> dict:
    datos_base = {
        "marca": {
            "nombre": "FIUNVA",
            "descripcion": "Soluciones de desarrollo, automatización y mantenimiento para clientes empresariales."
        },
        "servicios": {
            "que servicios ofrecen": "Ofrecemos desarrollo web, automatización industrial y mantenimiento de sistemas.",
            "horario": "Nuestro horario es de lunes a viernes de 9am a 6pm."
        },
        "faq_aprendidas": {}
    }
    return _cargar_json(MARCA_FILE, datos_base)


def guardar_marca(datos_marca: dict) -> None:
    _guardar_json(MARCA_FILE, datos_marca)
