'''
CONJUNTOS

En los conjuntos NO se pueden REPETIR los datos
porque no los almacena.
No se pueden meter dentro de cojuntos ni listas ni tuplas ni otros conjuntos
Los conjuntos son grupos de datos desordenados

'''
# Solo cuando creemos conjuntos vacios
conjunto01 = set()
conjunto01 = {}

# Crear un conjunto

conjunto01 = {0,1,2,3,4,'Patata', 7.9}

# agregar nuevos elementos. Que se van a insertar en lugares aleatorios(pero no random) siempre se escribira en el mismo sitio random

conjunto01.add('Uno')

print(conjunto01,'\n')

# Eliminar un valor 

conjunto01.discard('Patata')
print(conjunto01,'\n')

# Buscar elementos dentro de un conjunto
print(2 in conjunto01)
print(2 not in conjunto01,'\n')


# Comprobar  si ambos conjuntos son iguales
conjunto01 = {8,1,2}
conjunto02 = {3,4,1}
print(conjunto01 == conjunto02,'\n')

# Union de dos conjuntos 
union = conjunto01 |conjunto02
print(union,'\n')

# Interseccion de dos conjuntos. Los elementos que se repite
interseccion = conjunto01 & conjunto02
print(interseccion,'\n')

# La diferencia. Elementos que estan solo en el conjunto A
diferencia = conjunto01 - conjunto02
print(diferencia,'\n')

# La diferencia simetrica. Elementos que estan en A y B pero no en ambos
simetrica = conjunto01 ^ conjunto02
print(simetrica,'\n')

# Saber si es un subconjunto
conjunto03 = {1,2,3,4,5}
print(conjunto02.issubset(conjunto03),'\n')

# saber si un conjunto es un super conjunto
print(conjunto02.issuperset(conjunto03),'\n')

# saber si son disconexos
print(conjunto01.isdisjoint(conjunto03))

# conjunto sea inmutable
conjunto04 = frozenset({3,6,8,10})

# Borrar todo el contenido
conjunto01.clear()