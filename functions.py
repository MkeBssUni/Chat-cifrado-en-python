""" def cifrar(message, key):
  ciphertext = ""
  for char in message:
    ciphertext += chr((ord(char) + key) % 256)
  return ciphertext """

def cifrar(message, key):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    alfabeto_cifrado = alfabeto[key:] + alfabeto[:key]
    cifrado = ""
    for caracter in message:
        if caracter.isalpha():
            indice = alfabeto.find(caracter)
            if indice != -1:
                normal += caracter
                caracter_cifrado = alfabeto_cifrado[indice]
                cifrado += caracter_cifrado
        else:
            texto_normal += caracter
            texto_cifrado += caracter
    return cifrado
       



def descifrar(ciphertext, key):
    plaintext = ""
    for char in ciphertext:
        plaintext += chr((ord(char) - key) % 256)
    return plaintext

