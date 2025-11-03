from bot import buscar_respuesta

def main():
    historial = []
    print("Chatbot SoftDev (escribe 'salir' para terminar)\n")

    while True:
        user = input("Tú: ")
        if user.strip().lower() == "salir":
             print("Bot: ¡Hasta pronto!")
             break
        
        respuesta = buscar_respuesta(user)
        print("Bot:", respuesta)
        historial.append((user,respuesta))

    print("\n Historial de conversación:")
    for u, b in historial:
        print("Tú:", u)
        print("Bot:",b)

if __name__ == "__main__":
    main()