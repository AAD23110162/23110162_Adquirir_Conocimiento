# 23110162_Adquirir_Conocimiento

Chatbot de consola en Python para la marca FIUNVA.

## Funcionalidades

- Consulta de servicios generales de la marca.
- Consulta de estatus de proyectos por cliente.
- Registro de cliente nuevo cuando el código no existe.
- Flujo de cotización: captura de características, generación de borrador, confirmación y guardado.
- Aprendizaje dinámico de preguntas/respuestas no registradas.
- Salida limpia con `Ctrl + C` (sin traceback).

## Estructura del proyecto

```text
chatbot_proyectos/
├── app.py
├── core/
│   ├── __init__.py
│   ├── chatbot.py
│   ├── clientes.py
│   ├── cotizaciones.py
│   └── storage.py
└── data/
		├── clientes.json
		└── marca.json
```

## Descripción técnica de scripts Python

- `app.py`
	- Punto de entrada de la aplicación.
	- Ejecuta `ejecutar_chat()` y captura `KeyboardInterrupt` / `EOFError` para cerrar sin traceback.

- `core/chatbot.py`
	- Orquesta el ciclo principal del chat (`while` de interacción).
	- Detecta intención de consulta de servicios, estatus de proyectos y cotización.
	- Gestiona aprendizaje dinámico de respuestas nuevas en datos de marca.

- `core/clientes.py`
	- Login por `nombre + código`.
	- Registro de cliente nuevo si no existe.
	- Consulta de proyectos asociados al cliente autenticado.

- `core/cotizaciones.py`
	- Solicita características del proyecto.
	- Genera un borrador textual de cotización.
	- Confirma con el cliente y persiste cotización + estado inicial del proyecto.

- `core/storage.py`
	- Centraliza lectura/escritura JSON.
	- Define rutas de datos (`data/clientes.json`, `data/marca.json`).
	- Crea estructura base automáticamente si un archivo no existe.

## Organización de los JSON

- `data/clientes.json`
	- Contiene la raíz `clientes`.
	- Cada cliente se indexa por `código` y guarda:
		- `nombre`
		- `proyectos` (diccionario `nombre_proyecto -> estado`)
		- `cotizaciones` (lista de cotizaciones)
	- Cada cotización guarda:
		- `id`
		- `fecha_registro`
		- `estado`
		- `caracteristicas` (nombre, objetivo, alcance, tecnologías, presupuesto, fecha)
		- `borrador` (texto final mostrado al cliente)

- `data/marca.json`
	- `marca`: metadatos generales (`nombre`, `descripcion`).
	- `servicios`: preguntas frecuentes definidas manualmente.
	- `faq_aprendidas`: preguntas/respuestas aprendidas durante el uso del chatbot.

## Requisitos

- Python 3.10+

## Ejecución

```bash
cd chatbot_proyectos
python3 app.py
```

## Flujo de uso

1. Escribe una consulta general (ejemplo: `que servicios ofrecen`).
2. Para consultar estatus o cotizar, el bot solicita nombre y código de cliente.
3. Si el cliente no existe, ofrece crear un nuevo registro.
4. En cotización, solicita características del proyecto, muestra borrador y pide confirmación.
5. Si confirmas con `si`, guarda la cotización en `clientes.json`.

## Ejemplos de mensajes

- `que servicios ofrecen`
- `quiero consultar mi proyecto`
- `quiero cotizar un proyecto`
- `salir`

## Notas

- Si una pregunta no existe, el bot puede aprender una respuesta nueva y guardarla.
- Puedes finalizar en cualquier momento con `salir` o `Ctrl + C`.
