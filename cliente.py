import socket

def cifrar_mensaje(mensaje, clave):
    cifrado = ""
    for char in mensaje:
        if char.isalpha():
            cifrado += chr((ord(char) - 65 + clave) % 26 + 65) if char.isupper() else chr((ord(char) - 97 + clave) % 26 + 97)
        else:
            cifrado += char
    return cifrado

def main():
    # Configura el cliente
    host = '192.168.100.117'
    port = 5555

    # Crea un socket
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Conéctate al servidor
    client.connect((host, port))

    # Solicita la clave al usuario
    clave = int(input("Ingresa la clave de cifrado (número entero): "))

    while True:
        # Lee el mensaje del usuario
        message = input("Yo: ")

        # Cifra el mensaje antes de enviarlo usando la clave ingresada
        mensaje_cifrado = cifrar_mensaje(message, clave)

        # Envía el mensaje cifrado al servidor
        client.send(mensaje_cifrado.encode('utf-8'))

if __name__ == "__main__":
    main()
