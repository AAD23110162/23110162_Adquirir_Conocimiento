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

## Archivos de datos

- `data/clientes.json`
	- Datos de clientes
	- Proyectos por cliente
	- Cotizaciones registradas y borradores confirmados

- `data/marca.json`
	- Información general de la marca
	- Servicios ofrecidos
	- Preguntas aprendidas por el chatbot

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
