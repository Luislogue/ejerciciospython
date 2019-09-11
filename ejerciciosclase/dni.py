
def letraDNI(dni):

	letras="TRWAGMYFPDXBNJZSQVHLCKEO"
	valor=int(dni/23)
	valor*=23
	valor=dni-valor;
	return letras[valor]
 
dni = int(input('Introduzca su dni: '))
print(f'la letra del DNI es: {letraDNI(dni)}')