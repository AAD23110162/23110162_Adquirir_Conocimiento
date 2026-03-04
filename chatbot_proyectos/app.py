from core.chatbot import ejecutar_chat


if __name__ == "__main__":
    try:
        ejecutar_chat()
    except (KeyboardInterrupt, EOFError):
        print("\nBot: Sesión finalizada. Hasta luego.")
