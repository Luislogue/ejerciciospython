




nombre1 = str(input('Introduzca el nombre de la primera persona: '))
perA = int(input('Introduzca edad de la primera persona: '))
nombre2 = str(input('Introduzca el nombre de la segunda persona: '))
perB = int(input('Introduzca edad de la segunda persona: '))
nombre3 = str(input('Introduzca el nombre de la tercera persona: '))
perC = int(input('Introduzca edad de la tercera persona: '))

if perA > perB > perC:
    diferencia = perA - perB
    dif = perA - perC
    print(f'{nombre1} es mayor y le saca {diferencia} años a {nombre2} y {dif} a {nombre3}')
elif perB > perA > perC:
    diferencia = perB - perA
    dif = perB - perC
    print(f'{nombre2} es mayor y le saca {diferencia} años a {nombre1} y {dif} a {nombre3}')
elif perC > perA > perB:
    diferencia = perC -perA
    dif = perC - perB
    print(f'{nombre3} es mayor y le saca {diferencia} años a {nombre1} y {dif} a {nombre2}')