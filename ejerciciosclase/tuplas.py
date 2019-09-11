'''
TUPLAS 
SIRVEN PARA BUSCAR
CONSUMEN MENOS MEMORIA
SON MAS RAPIDAS
pero
DESPUES DE CREARLAS SON INMODIFICABLES
'''

tupla01 = ('Lunes', 'Martes', 'Miercoles')

print(tupla01,'\n')

# Longitud de esta tupla

print(len(tupla01),'\n')

# Saber si un valor esta dentro de la tupla

print('Martes' in tupla01)

# Saber en que posicion esta un elemento

print(tupla01.index('Miercoles'))

#Contar cuantos miercoles 

print(tupla01.count('Miercoles'))

# Copiar el contenido de una tupla a una lista

nuevaLista = list(tupla01)
print(nuevaLista,'\n')

# Copiar el contenido de una lista a una tupla

nuevaTupla = tuple(nuevaLista)
print(nuevaTupla,'\n')