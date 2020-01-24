# Ejercicio 3
#   Determina el mayor número que más se repite y su cantidad de ocurrencias
#       Input: [1,1,2,2,2,3,3,3,2]
#       Output: 2, 4

entry = input('Ingrese lista a verificar: ')
entryList = entry[entry.find('[')+1 : entry.find(']')].split(',')
counter = dict.fromkeys(entryList,0)

for i in entryList :
    counter[i] += 1

maxTuple = max(zip(counter.values(),counter.keys()))

print("{}, {}".format(maxTuple[1],maxTuple[0]))