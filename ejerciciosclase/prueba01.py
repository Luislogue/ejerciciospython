# Variables
# *********

nombre = 'Dabid'
apodo = 'gae'

print('El ' + nombre+ ' ' + 'es ' + apodo)

# Calcular el area de un circulo

pi = 3.14159
radio = 3

area = pi * radio**2

print(area)
# Entrada de datos

nombre = str(input('Cual es tu nombre? '))
print(nombre + ' ' + 'eres gay')

# Prioridades de operadores genericos
# *************************
# 1.()
# 2.**
# 3.*, /, mod, not
# 4. +, -, and
# 5. >, <, ==, >=, <=, !=, or


#forma1 
# print('Hola me llamo', nombre, 'y mido', altura,'metros de estatura')
# forma2
# print('Hola me llamo {} y mido {} metros').format(nombre, altura)

# forma2
# print(f'Hola me llamo{nombre} y mido {altura} metros de estatura')

# Entrada de datos
# ***********
# Input te guarda datos tipo cadena
nombre = input('Tu nombre: ')

# input guardar valores numericos
edad = int(input('Tu edad: '))
altura = float(input('Tu altura: '))

print(f'Hola {nombre} tienes {edad} años y mides {altura} m')

# FUNCIONES INTEGRADADAS
# convertir string en entero

n = int('10')
print(n)
# convertir un string a decimal
n = float('10.4')
print(n)
# Convertir integer a string
n = str(10)
print(n)
# Convertir un numero a binario
n = bin(10)
print(n)
# Convertir un numero a hexadecimal
n = hex(10)
print(n)
# Convertir un binario en entero
n = int('0b1010', 2)
print(n)
# Convertir un binario
n = int('0xa', 16)
print(n)
# Convertir un negativo a positivo 
n = abs(-12)
print(n)
# Convertir un numero decimal en entero
n = round(6.8)
print(n)
#CANTIDAD DE CARACTERES
n = len('Luis')
print(n)

