
import math

numero = float(input('Introduzca un numero: '))

while numero < 0:
    print('Error, debe escribir un numero positivo')
    numero =  float(input('Introduzca un numero: '))

print(f'\nSu raiz cuadrada es: {(math.sqrt(numero)):.2f}','\n')

# Variable iteradora

i = 2
while i < 4:
    print('Hola mundo')
    # i++ :
    i += 1 

print('FINAL')