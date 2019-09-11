'''
LISTAS
Parecidas a los arreglos
'''

grupo = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo', 20, True, 0.42]

# Multiplicar elementos de una lista
grupo = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo', 20, True, 0.42] * 4

# imprimir elementos de una lista

print(grupo,'\n')

# imprimir elementos seleccionados de una lista

print(grupo[2:5], '\n')

# agregar elementos al final de una lista

grupo.append('FINAL')

print(grupo,'\n')

# agregar elementos en una lista
grupo.insert(2,'CENTRO')
print(grupo,'\n')

# Agregar varios elementos
grupo.extend([20,'patata,',False])
print(grupo,'\n')

# Concatenar listas 
otroGrupo = ['perro','gato', 'laLara','lamaedelalexis']

grupoFinal = grupo + otroGrupo
print(grupoFinal,'\n')

# saber si un valor esta dentro de una lista

print(20 in grupoFinal)

# Saber en que indice esta el elemento

print(grupoFinal.index('laLara'))

# Contar cuantas veces se repite un elemento

print(grupoFinal.count('Lunes'))

# eliminar siempre el ultimo elemento de la lista
grupoFinal.pop()
print(grupoFinal,'\n')

# eliminar el elemento que queramos de la lista
grupoFinal.pop(5)
print(grupoFinal,'\n')

# eliminar el elemento exacto de una lista
grupoFinal.remove('FINAL')
print(grupoFinal)

# Voltear un lista
grupoFinal.reverse()
print(grupoFinal)

# Ordenar una lista del mismo tipo de variables
'''
grupoFinal.sort()
grupoFinal.sort(reverse=True)
'''
# Borrar todo el contenido de la lista

grupoFinal.clear()

# Cambiar un elemento de la lista 

grupoFinal[5] = 'Cosa'

print(grupoFinal)

