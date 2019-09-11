'''
DICCIONARIOS
Elementos desorden por todas partes

'''
# Diccionario vacio

diccionario = {}

# diccionario

diccionario = {
    'rojo': 'red',
    'lapiz': 'pencil'
}
print(diccionario,'\n')

# sacar el resultado de una llave

print(diccionario['lapiz'],'\n')

# agregar nuevos elementos

diccionario['perro'] = 'dog'
print(diccionario,'\n')

# Modificar elementos de un diccionario
diccionario['rojo'] = 'red'
print(diccionario,'\n')

# eliminar un elemento
del(diccionario['rojo'])
print(diccionario)

# *****

agenda = {
    'Pepe' : [33, 1.72],
    'Maria': [24, 1.80],
    'Juan' : [44, 1.64],
    'Eva' : [14, 1.45]
}

print(agenda['Maria'],'\n')

# *******
agenda01 = {
    'Pepe':{'edad':33, 'altura':1.62},
    'Maria':{'edad':24, 'altura':1.80},
    'Juan':{'edad':44, 'altura':1.64},
    'Eva':{'edad':44, 'altura':1.64}
}
print(agenda01['Eva'],'\n')

# *******
equipoNBA = {
    23:'Michael Jordan',
    00:'Robert Parish',
    21:'Dominique Wilkins',
    33:'Larry Bird',
    10:'Dennis Rodman',
    34:'Shaquille Oneile',
    24:'Moses Malone',
}

# sacar el valor, sabiendo que existe la llave
print(equipoNBA[00],'\n')
# si no sabes si existe la llave
print(equipoNBA.get(23,'No existe'),'\n')
# busqueda directa
print(33 in equipoNBA,'\n')
# Enseñar solo las key's
print(equipoNBA.keys())

# enseñar solo valores
print(equipoNBA.values(),'\n')

# enseñame la llave con el valorde todos
print(equipoNBA.items(),'\n')