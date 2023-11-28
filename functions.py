def cifrar(message, key):
  """Cifra un mensaje usando el método Cesar.

  Args:
    message: El mensaje a cifrar.
    key: La clave de cifrado.

  Returns:
    El mensaje cifrado.
  """

  ciphertext = ""
  for char in message:
    ciphertext += chr((ord(char) + key) % 256)
  return ciphertext
