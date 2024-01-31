
import afin
import caesar
import vigenere

distribuciones_wikipedia = {
    'A': 12.53, 'B': 1.42, 'C': 4.68, 'D': 5.86, 'E': 13.68, 'F': 0.69,
    'G': 1.01, 'H': 0.70, 'I': 6.25, 'J': 0.44, 'K': 0.02, 'L': 4.97,
    'M': 3.15, 'N': 6.71, 'Ñ': 0.31, 'O': 8.68, 'P': 2.51, 'Q': 0.88,
    'R': 6.87, 'S': 7.98, 'T': 4.63, 'U': 3.93, 'V': 0.90, 'W': 0.01,
    'X': 0.22, 'Y': 0.90, 'Z': 0.52
}

def calcular_distribucion(texto):
    alfabeto = "abcdefghijklmnñopqrstuvwxyz"
    frecuencias = dict.fromkeys(alfabeto, 0)
    total_caracteres = 0

    texto = texto.lower().replace(" ", "")  
    for letra in texto:
        if letra in alfabeto:
            frecuencias[letra] += 1
            total_caracteres += 1

    for letra in frecuencias:
        frecuencias[letra] = (frecuencias[letra] / total_caracteres) * 100 if total_caracteres > 0 else 0

    return frecuencias

def ordenar_distribucion(distribucion):
    return dict(sorted(distribucion.items(), key=lambda x: x[1], reverse=True))


def filtrar_distribucion(distribucion):
    return {letra: frec for letra, frec in distribucion.items() if frec > 0}

def lado_a_lado(distribucion_ordenada, distribuciones_wikipedia):
    for letra, frec in distribucion_ordenada.items():
        frec_wikipedia = distribuciones_wikipedia.get(letra.upper(), 0)
        print(f"{letra.upper()}: {frec:.2f}% - Wikipedia: {frec_wikipedia:.2f}%")



mensaje = "Patito feo o lindo"
mensaje_cifrado_caesar= caesar.cifrado_cesar(mensaje)
print("Mensaje cifrado:", mensaje_cifrado_caesar)
distribucion = calcular_distribucion(mensaje_cifrado_caesar)
distribucion_ordenada = ordenar_distribucion(distribucion)
distribucion_filtrada = filtrar_distribucion(distribucion_ordenada)
print("Distribución de frecuencias:")
lado_a_lado(distribucion_filtrada, distribuciones_wikipedia)




#Sumar cuantas veces se suma una palabra en un texto 
#ej: patitofeolindo
#p:1
#a:2
#t:2
#i:1
#f:1
#e:1
#o:1
#l:1
#n:1
#d:1
#genera probabilidad de cada letra 