'''
def comparar(x, y, z):
    if x > y and x > z:
        return(f'{x} es mayor que {y} y que {z}')
    if x == y and x > z:
        return(f'{x} es igual que {y} y mayor que {z}')
    if y > x and y > z:
        return(f'{y} es mayor que {x} y que {z}')
    if y == x and y > z:
        return(f'{y} es igual que {x} y mayor que {z}')
    if z > x and z > y:
        return(f'{z} es mayor que {x} y que {y}')
    if z == x and z > y:
        return(f'{z} es igual que {x} y mayor que {y}')
    if z == y and z > x:
        return(f'{z} es igual que {y} y mayor que {x}')
    else:
        return('son iguales')


if __name__ == '__main__':
    x = float(input('Escriba el primer numero: '))
    y = float(input('Escriba el segundo numero: '))
    z = float(input('Escriba el tercer numero: '))

    print(comparar(x, y, z))
'''

def menorque():
    a = float(input('a -> '))
    b = float(input('b -> '))
    c = float(input('c -> '))

    tres = [a, b, c]
    tres.sort(reverse=True)
    print(f'Numero mayor: {tres[0]}')
    tres.reverse()
    print(f'Numero menor: {tres[0]}')
    print(f'El numero intermedio es: {tres[1]}')

    conj = set(tres)
    return( a | b | c)

menorque()