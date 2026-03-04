from core.storage import guardar_clientes


def autenticar_o_registrar_cliente(datos_clientes: dict) -> str | None:
    nombre = input("Ingrese su nombre: ").strip()
    codigo = input("Ingrese su código de cliente: ").strip()

    clientes = datos_clientes.setdefault("clientes", {})

    if codigo in clientes:
        nombre_registrado = clientes[codigo].get("nombre", "")
        if nombre_registrado.lower() == nombre.lower():
            print(f"Bienvenido nuevamente, {nombre}.")
            return codigo

        print("Nombre incorrecto para ese código.")
        return None

    crear = input("Cliente no encontrado. ¿Desea crear uno nuevo? (si/no): ").strip().lower()
    if crear != "si":
        print("No se creó el cliente.")
        return None

    clientes[codigo] = {
        "nombre": nombre,
        "proyectos": {},
        "cotizaciones": []
    }
    guardar_clientes(datos_clientes)
    print("Cliente creado correctamente.")
    return codigo


def consultar_proyectos(datos_clientes: dict, codigo_cliente: str) -> None:
    cliente = datos_clientes.get("clientes", {}).get(codigo_cliente)
    if not cliente:
        print("No se encontró información del cliente.")
        return

    proyectos = cliente.get("proyectos", {})
    if not proyectos:
        print("No tiene proyectos registrados.")
        return

    print("Proyectos encontrados:")
    for nombre_proyecto, estado in proyectos.items():
        print(f"- {nombre_proyecto}: {estado}")
