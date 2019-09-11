'''
GENERADORES EN PYTHON

Son estructuras que extraen valores de una funcion 
se almacenan en objetos iterantes.
Los valroes se almacenan de uno en uno 
Cuando se almacenan ese valor "suspension de estado"
'''
# Funcion
def pares():
    limite = int(input("Por favor, introduzca el limite: "))
    num = 1
    numList = []

    while num < limite:
        numList.append(num * 2)

        num += 1

    return numList


if __name__ == "__main__":
    pares()

# Generador

def num_pares_generador():
    limite = int(input("Por favor, introduzca el limite: "))
    num = 1
    # No es necesario una lista

    while num < limite:
        # Construye un objeto iterable
        # Almacenando los elementos de 1 en 1

        yield num * 2

        num += 1

resultado = num_pares_generador()
# for i in resultado:
#     print(i)
print(next(resultado))
print(next(resultado))
print(next(resultado))
print(next(resultado))