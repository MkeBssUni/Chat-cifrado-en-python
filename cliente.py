import socket
import functions as f

def main():
  # Configura el cliente
  host = 'localhost'
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
    mensaje_cifrado = f.cifrar_mensaje(message, clave)

    # Envía el mensaje cifrado al servidor
    client.send(mensaje_cifrado.encode('utf-8'))

    # Recibe el mensaje cifrado del servidor
    mensaje_cifrado = client.recv(1024).decode('utf-8')

    if not mensaje_cifrado:
      # Si no hay mensaje, rompe el bucle
      break

    # Muestra el mensaje cifrado recibido
    print(f"Mensaje cifrado: {mensaje_cifrado}")

    # Descifra el mensaje usando la clave ingresada
    mensaje_descifrado = f.descifrar_mensaje(mensaje_cifrado, clave)

    # Muestra el mensaje descifrado
    print(f"Mensaje descifrado: {mensaje_descifrado}")


  # Cierra la conexión
  client.close()

if __name__ == "__main__":
    main()
