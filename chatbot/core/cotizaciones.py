from datetime import datetime

from core.storage import guardar_clientes


def solicitar_caracteristicas_proyecto() -> dict:
    print("\nVamos a crear una cotización. Ingrese la información del proyecto:")

    return {
        "nombre_proyecto": input("Nombre del proyecto: ").strip(),
        "objetivo": input("Objetivo principal: ").strip(),
        "alcance": input("Alcance (qué incluye): ").strip(),
        "tecnologias": input("Tecnologías o plataforma deseada: ").strip(),
        "presupuesto_estimado": input("Presupuesto estimado: ").strip(),
        "fecha_deseada": input("Fecha deseada de entrega: ").strip()
    }


def generar_borrador(nombre_cliente: str, codigo_cliente: str, caracteristicas: dict) -> str:
    return (
        "\n--- BORRADOR DE PROYECTO ---\n"
        f"Cliente: {nombre_cliente} (Código: {codigo_cliente})\n"
        f"Proyecto: {caracteristicas['nombre_proyecto']}\n"
        f"Objetivo: {caracteristicas['objetivo']}\n"
        f"Alcance: {caracteristicas['alcance']}\n"
        f"Tecnologías/plataforma: {caracteristicas['tecnologias']}\n"
        f"Presupuesto estimado: {caracteristicas['presupuesto_estimado']}\n"
        f"Fecha deseada: {caracteristicas['fecha_deseada']}\n"
        "Estado inicial: Borrador confirmado por cliente\n"
        "-----------------------------"
    )


def confirmar_y_guardar_cotizacion(datos_clientes: dict, codigo_cliente: str, caracteristicas: dict, borrador: str) -> bool:
    cliente = datos_clientes["clientes"][codigo_cliente]
    cotizaciones = cliente.setdefault("cotizaciones", [])

    print(borrador)
    confirmar = input("\n¿Confirma este borrador para guardarlo? (si/no): ").strip().lower()
    if confirmar != "si":
        print("Cotización cancelada, no se guardó información.")
        return False

    nueva_cotizacion_id = f"COT-{len(cotizaciones) + 1:03d}"
    cotizacion = {
        "id": nueva_cotizacion_id,
        "fecha_registro": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "estado": "Borrador confirmado",
        "caracteristicas": caracteristicas,
        "borrador": borrador
    }
    cotizaciones.append(cotizacion)

    nombre_proyecto = caracteristicas["nombre_proyecto"]
    cliente.setdefault("proyectos", {})[nombre_proyecto] = "Cotización recibida - En revisión comercial"

    guardar_clientes(datos_clientes)
    print(f"Cotización {nueva_cotizacion_id} guardada correctamente.")
    return True
