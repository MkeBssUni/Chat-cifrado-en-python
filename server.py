import socket
import functions as f

def main():
  # Configura el servidor
  host = 'localhost'
  port = 5555

  # Crea un socket
  server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  # Enlaza el socket al host y al puerto
  server.bind((host, port))

  # Escucha las conexiones entrantes
  server.listen()

  print("Esperando conexiones...")

  # Acepta la conexión
  client_socket, client_addr = server.accept()
  print(f"Conexión establecida con {client_addr}")

  # Solicita la clave al servidor para descifrar el primer mensaje
  clave = int(input("Introduce la clave de cifrado para descifrar el primer mensaje: "))

  while True:
    # Recibe el mensaje cifrado
    mensaje_cifrado = client_socket.recv(1024).decode('utf-8')

    if not mensaje_cifrado:
      # Si no hay mensaje, rompe el bucle
      break

    # Muestra el mensaje cifrado recibido
    print(f"Mensaje cifrado: {mensaje_cifrado}")

    # Descifra el mensaje usando la clave ingresada
    mensaje_descifrado = f.descifrar_mensaje(mensaje_cifrado, clave)

    # Muestra el mensaje descifrado
    print(f"Mensaje descifrado: {mensaje_descifrado}")

    # Crea un nuevo mensaje
    mensaje = input("Yo: ")

    # Cifra el mensaje usando la clave de cifrado compartida
    mensaje_cifrado = f.cifrar_mensaje(mensaje, clave)

    # Envia el mensaje al cliente
    client_socket.send(mensaje_cifrado.encode('utf-8'))

  # Cierra la conexión
  client_socket.close()
  server.close()

if __name__ == "__main__":
    main()
