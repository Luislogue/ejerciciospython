a = float(input('Introduzca el primer numero: '))
b = float(input('Introduzca el segundo numero: '))

op = str(input('Introduzca el operador que quiere(+, -, *, /): '))

if op == '+' or op == 'sumar' or op == 's' :
    suma = (a + b)
    print(suma)
elif op == '-' or op == 'restar' or op == 'r':
    resta = (a - b)
    print(resta)
elif op == '*' or op == 'multiplicar' or op == 'm':
    multi = (a * b)
    print(multi)
elif op == '/' or op == 'dividir' or op == 'd':
    div = (a / b)
    print(div)

