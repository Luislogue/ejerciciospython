'''
TEOREMA DE PITAGORAS
'''

import math

a = float(input('Introduzca el cateto 1: '))
b = float(input('Introduzca el cateto 2: '))


c = (a**2) + (b**2)

sol = math.sqrt(c)
print(f'El resultado es: {sol:.2f}')
# :.2f sacara 2 decimales en el resultado