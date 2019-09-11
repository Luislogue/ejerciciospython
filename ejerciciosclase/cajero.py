saldo = 4000
# ingresar retirar salir mostrar

accion = str(input('Que desea hacer?\n ingresar\n retirar\n mostrar\n salir: '))

if accion == 'ingresar':
    ingreso = float(input('Que cantidad desearia ingresar?: '))
    saldo = saldo + ingreso
    print(f'Perfecto, han sido ingresados{ingreso:.2f} euros en su cuenta, su saldo actual es de {saldo:.2f}')
if accion == 'retirar':
    retirada = float(input(f'Su saldo es de {saldo:.2f} euros, que cantidad desea retirar?: '))
    if retirada <= saldo:
        saldo = (saldo - retirada)
        print(f'Perfecto, han sido retirados {retirada:.2f} euros de su cuenta, su balance actual es de {saldo:.2f} euros')
    if retirada > saldo:
        print('Lo sentimos, no puede retirar una cantidad mayor que su saldo, si quiere un prestamo pase a la oficina')
if accion == 'mostrar':
    print(f'Su saldo es de: {saldo:.2f}')
if accion == 'salir':
    print('Gracias por elegirnos, hasta pronto')
    