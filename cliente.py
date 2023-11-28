import socket

def main():
    # Configura el cliente
    host = '127.0.0.1'
    port = 5555

    # Crea un socket
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Conéctate al servidor
    client.connect((host, port))

    while True:
        # Lee el mensaje del usuario
        message = input("Yo: ")
        
        # Envía el mensaje al servidor
        client.send(message.encode('utf-8'))

if __name__ == "__main__":
    main()
