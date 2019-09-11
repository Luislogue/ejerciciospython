
import math

'''
FOR 
es el bucle que se utiliza en las colecciones

'''
for i in [1,'Hola',3,4,5,6]:
    print('Adios')

coleccion = (1,2,3,4,5)

for i in coleccion:
    print(f'Elemento: {i}')

coleccion01 = {
    'Pepe': 34,
    'Maria': 67,
    'Jose': 44
}

# saca la llave valor
for i in coleccion01:
    print(f'{i} -> {coleccion01[i]}')

# otro metodo 
for llave, valor in coleccion01.items():
    print(f'{llave} -> {valor}')