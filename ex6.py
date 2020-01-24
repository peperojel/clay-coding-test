# Ejercicio 6
#   Indica la secuencia de números a presionar de N oraciones en minúscula.
#       N: Cantidad definida por el usuario al inicio del programa
#           Input: hello
#           Output: ​4433555 555666096667775553

N = input('Indique la cantidad de casos de prueba: ')
counter = 0

dictTranslator = {
    'a': '2', 'b': '22', 'c': '222',
    'd': '3', 'e': '33', 'f': '333',
    'g': '4', 'h': '44', 'i': '444',
    'j': '5', 'k': '55', 'l': '555',
    'm': '6', 'n': '66', 'o': '666',
    'p': '7', 'q': '77', 'r': '777', 's': '7777',
    't': '8', 'u': '88', 'v': '888',
    'w': '9', 'x': '99', 'y': '999', 'z': '9999',
    ' ': '0'
}

while True:
    counter += 1
    inStr = list(input('Input: '))
    outSeq = dictTranslator[inStr[0]]

    for i in range(1,len(inStr)):
        if(list(outSeq)[-1] == list(dictTranslator[inStr[i]])[0]):
            outSeq += ' ' + dictTranslator[inStr[i]]
        else:
            outSeq += dictTranslator[inStr[i]]

    print('Output:', outSeq)

    if (counter == int(N)):
        break
