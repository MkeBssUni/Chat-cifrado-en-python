""" def cifrar(message, key):
  ciphertext = ""
  for char in message:
    ciphertext += chr((ord(char) + key) % 256)
  return ciphertext """

def cifrar(message, key):
  ciphertext = ""
  for char in message:
    # Calcula la posición del carácter en el alfabeto.
    position = ord(char) - ord('a')

    # Calcula la posición del nuevo carácter.
    new_position = (position + key) % 26

    # Convierte la posición del nuevo carácter a un carácter.
    new_char = chr(new_position + ord('a'))

    ciphertext += new_char
  return ciphertext


def descifrar(ciphertext, key):
  # descifra un mensaje usando el método Cesar y una clave de cifrado
    plaintext = ""
    for char in ciphertext:
      plaintext += chr((ord(char) - key) % 256)
    return plaintext

