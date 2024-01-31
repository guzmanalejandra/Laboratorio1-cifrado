#caesar cipher
import math

alfabeto = "abcdefghijklmnñopqrstuvwxyz"

def cifrado_cesar(mensaje):
    mensaje = mensaje.lower()
    mensaje_cifrado = ""
    for letra in mensaje:
        if letra in alfabeto:
            indice = alfabeto.index(letra)
            indice_nuevo = indice + 3 
            if indice_nuevo >= len(alfabeto):  
                indice_nuevo = indice_nuevo - len(alfabeto)
            mensaje_cifrado = mensaje_cifrado + alfabeto[indice_nuevo]
        else:
            mensaje_cifrado = mensaje_cifrado + letra
    return mensaje_cifrado


def descifrado_cesar(mensaje):
    mensaje = mensaje.lower()
    mensaje_descifrado = ""
    for letra in mensaje:
        if letra in alfabeto:
            indice = alfabeto.index(letra)
            indice_nuevo = indice - 3
            if indice_nuevo >= len(alfabeto):  
                indice_nuevo = indice_nuevo + len(alfabeto)
            mensaje_descifrado = mensaje_descifrado + alfabeto[indice_nuevo]
        else:
            mensaje_descifrado = mensaje_descifrado + letra
    return mensaje_descifrado
 
#mensaje = "patito feo dice hola"   
#print("Mensaje para cifrar:", mensaje)
#resultado = cifrado_cesar(mensaje)
#print("Mensaje cifrado: ", resultado)
#descifrado = descifrado_cesar(resultado)
#print("Mensaje descifrado:", descifrado)





    