import socket
import threading

def cifrar_mensaje(mensaje):
    cifrado = ""
    for char in mensaje:
        if char.isalpha():
            cifrado += chr((ord(char) - 65 + 3) % 26 + 65) if char.isupper() else chr((ord(char) - 97 + 3) % 26 + 97)
        else:
            cifrado += char
    return cifrado

def handle_client(client_socket, address):
    while True:
        # Espera a recibir datos del cliente
        data = client_socket.recv(1024).decode('utf-8')
        if not data:
            break

        # Descifra el mensaje recibido
        mensaje_descifrado = cifrar_mensaje(data)

        print(f"Mensaje de {address[0]}:{address[1]}: {mensaje_descifrado}")

    client_socket.close()

def main():
    # Configura el servidor
    host = '0.0.0.0'
    port = 5555

    # Crea un socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)

    print(f"[*] Servidor escuchando en {host}:{port}")

    while True:
        # Acepta conexiones entrantes
        client, address = server.accept()
        print(f"[*] Conexión aceptada de {address[0]}:{address[1]}")

        # Inicia un hilo para manejar la conexión del cliente
        client_handler = threading.Thread(target=handle_client, args=(client, address))
        client_handler.start()

if __name__ == "__main__":
    main()
