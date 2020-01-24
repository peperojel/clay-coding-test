# Ejercicio 5
#   Verifica si N oraciones son o no pangramas.
#       N: Cantidad definida por el usuario al inicio del programa
#           Input: "The quick brown fox jumps over the lazy dog"
#           Output: "SI"

alfabeto = set('abcdefghijklmnopqrstuvwxyz')

def checkPangram (inputString):
    inputSet = set(inputString.lower())
    if (alfabeto.union(inputSet) == inputSet):
        return 'SI'
    else:
        return 'NO'

repets = input('Indique la cantidad de oraciones a analizar: ')
counter = 0

while True:
    inputString = input('Input: ')
    counter += 1
    print('Output:', checkPangram(inputString))
    if (counter == int(repets)):
        break