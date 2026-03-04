from core.clientes import autenticar_o_registrar_cliente, consultar_proyectos
from core.cotizaciones import (
    confirmar_y_guardar_cotizacion,
    generar_borrador,
    solicitar_caracteristicas_proyecto,
)
from core.storage import cargar_clientes, cargar_marca, guardar_marca


def _buscar_respuesta_servicio(datos_marca: dict, mensaje: str) -> str | None:
    servicios = datos_marca.get("servicios", {})
    faq_aprendidas = datos_marca.get("faq_aprendidas", {})

    if mensaje in servicios:
        return servicios[mensaje]

    if mensaje in faq_aprendidas:
        return faq_aprendidas[mensaje]

    return None


def _aprender_respuesta(datos_marca: dict, mensaje: str) -> None:
    print("Bot: No tengo información sobre eso.")
    nueva_respuesta = input("¿Cuál debería ser la respuesta? (o escriba 'no'): ").strip()

    if nueva_respuesta.lower() == "no" or not nueva_respuesta:
        return

    datos_marca.setdefault("faq_aprendidas", {})[mensaje] = nueva_respuesta
    guardar_marca(datos_marca)
    print("Bot: Gracias, he aprendido algo nuevo 😎")


def ejecutar_chat() -> None:
    datos_clientes = cargar_clientes()
    datos_marca = cargar_marca()
    codigo_cliente_activo = None

    nombre_marca = datos_marca.get("marca", {}).get("nombre", "la marca")
    print(f"🤖 Bienvenido al asistente de {nombre_marca}.")
    print("Puede consultar servicios, estatus de proyectos o solicitar cotización.")
    print("Escriba 'salir' para terminar.")

    while True:
        mensaje = input("\nTú: ").strip().lower()

        if not mensaje:
            continue

        if mensaje == "salir":
            print("Bot: Hasta luego.")
            break

        if "cotiz" in mensaje:
            if not codigo_cliente_activo:
                codigo_cliente_activo = autenticar_o_registrar_cliente(datos_clientes)

            if not codigo_cliente_activo:
                continue

            cliente = datos_clientes["clientes"][codigo_cliente_activo]
            caracteristicas = solicitar_caracteristicas_proyecto()
            borrador = generar_borrador(cliente["nombre"], codigo_cliente_activo, caracteristicas)
            confirmar_y_guardar_cotizacion(datos_clientes, codigo_cliente_activo, caracteristicas, borrador)
            continue

        if "proyecto" in mensaje or "estatus" in mensaje:
            if not codigo_cliente_activo:
                codigo_cliente_activo = autenticar_o_registrar_cliente(datos_clientes)

            if codigo_cliente_activo:
                consultar_proyectos(datos_clientes, codigo_cliente_activo)
            continue

        respuesta = _buscar_respuesta_servicio(datos_marca, mensaje)
        if respuesta:
            print("Bot:", respuesta)
            continue

        _aprender_respuesta(datos_marca, mensaje)
