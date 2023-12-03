def cifrar_mensaje(mensaje, clave):
    cifrado = ""
    for char in mensaje:
        if char.isalpha():
            cifrado += chr((ord(char) - 65 + clave) % 26 + 65) if char.isupper() else chr((ord(char) - 97 + clave) % 26 + 97)
        else:
            cifrado += char
    return cifrado


def descifrar_mensaje(mensaje, clave):
  descifrado = ""
  for char in mensaje:
    if char.isalpha():
      descifrado += chr((ord(char) - 65 - clave) % 26 + 65) if char.isupper() else chr((ord(char) - 97 - clave) % 26 + 97)
    else:
      descifrado += char
  return descifrado