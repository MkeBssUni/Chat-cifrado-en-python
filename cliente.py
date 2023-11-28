# cliente.py
from functions import cifrar
import socket

def main():
  # Configura el cliente
  host = '192.168.100.109'
  port = 5555

  # Crea un socket
  client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  # Conéctate al servidor
  client.connect((host, port))

  # Pide al usuario que ingrese una clave de cifrado
  key = input("Ingrese la clave de cifrado: ")

  while True:
    # Lee el mensaje del usuario
    message = input("Yo: ")

    # Cifra el mensaje
    ciphertext = cifrar(message, int(key))

    # Envía el mensaje cifrado al servidor
    client.send(ciphertext.encode('utf-8'))

if __name__ == "__main__":
  main()
