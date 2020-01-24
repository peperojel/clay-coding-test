# Ejercicio 4
#   Entrega la fecha del siguiente día habil (Lu-Vi)
#       Input: 24-01-2020
#       Output: 27-01-2020

from datetime import date, timedelta

inputDate = input('Ingrese el dia actual: ').split('-')

inputDate = date(int(inputDate[2]), int(inputDate[1]), int(inputDate[0]))
day = inputDate.weekday()

if (day in [0,1,2,3]) :
    outDate = inputDate + timedelta(1)
else:
    outDate = inputDate + timedelta([3,2,1][day-4])

print(outDate.strftime("%d-%m-%Y"))