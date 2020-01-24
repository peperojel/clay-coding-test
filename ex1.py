# Ejercicio 1
#   Traduce un número decimal a su representación en romano
#       Input: 14
#       Output: XIV

dec_num = input('Input: ')
roman_num = ''

rom_cent = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
rom_dece = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
rom_unit = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']

if (int(dec_num) > 3999) :
    print('Número debe ser menor a 3999')
    exit()
    
mile = int(dec_num) // 1000
cent = (int(dec_num) - mile*1000) // 100
dece = (int(dec_num) - mile*1000 - cent*100) // 10
unit = int(dec_num) - mile*1000 - cent*100 - dece*10

if (mile) :
    roman_num += 'M'*mile
if (cent) :
    roman_num += rom_cent[cent]
if (dece) :
    roman_num += rom_dece[dece]
if (unit) :
    roman_num += rom_unit[unit]

print('Output:',roman_num)