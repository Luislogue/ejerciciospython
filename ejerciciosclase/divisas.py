'''
Calculadora de divisas
1 Libras -> 1.11 Euros
1 Euros -> 1.11 Libras
'''
def menu():
    divisa = str(input("Introduzca la moneda que desea cambiar: "))
    cantidad = float(input("Introduzca la cantidad que desea cambiar: "))
    if divisa == "libra" or divisa == "libras":
        total = cantidad * 1.11
        print(f'Sus: {cantidad} libras seran convertidas a: {total} €')
    if divisa == "euro" or divisa == "euros":
        total = cantidad / 1.11
        print(f'Sus: {total} € seran convertidas a: {divisa} libras')



if __name__ == "__main__":

    menu()
    
