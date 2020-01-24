# Ejercicio 2
#   Determina si un número entero está presente en una lista.
#       Input: [1,2,3,4],4
#       Output: True

entry = input('Input: ')

lookFor = entry.split(',').pop()
inList = entry[entry.find('[')+1 : entry.find(']')].split(',')

for i in inList :
    if(i == lookFor):
        print('Output:', True)
        exit()

print('Output:', False)