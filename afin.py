import math

alfabeto = "abcdefghijklmnñopqrstuvwxyz"

def cifrado_afin(mensaje, a, b):
    mensaje = mensaje.lower()
    mensaje_cifrado = ""
    for letra in mensaje:
        if letra in alfabeto:
            indice = alfabeto.index(letra)
            indice_nuevo = (a * indice + b) % len(alfabeto)
            mensaje_cifrado += alfabeto[indice_nuevo]
        else:
            mensaje_cifrado += letra
    return mensaje_cifrado

def descifrado_afin(mensaje, a, b):
    mensaje = mensaje.lower()
    mensaje_descifrado = ""
    a_inv = pow(a, -1, len(alfabeto))
    for letra in mensaje:
        if letra in alfabeto:
            indice = alfabeto.index(letra)
            indice_nuevo = (a_inv * (indice - b)) % len(alfabeto)
            mensaje_descifrado += alfabeto[indice_nuevo]
        else:
            mensaje_descifrado += letra
    return mensaje_descifrado

mensaje = "cupa"
a = 5
b = 12

#print("Mensaje para cifrar:", mensaje)
#cifrar = cifrado_afin(mensaje, a, b)
#print("Mensaje cifrado:", cifrar)
#descifrar = descifrado_afin(cifrar, a, b)
#print("Mensaje descifrado:", descifrar)
