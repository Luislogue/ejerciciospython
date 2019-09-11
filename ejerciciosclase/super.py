''' 
3Compras de cantidad X
Si la compra excede los 50 euros, 15% descuento
Si es menor de 30 le diremos que si llega a 50 tendra descuento
Entre 0 y 20 nada 
'''

print('Buenos dias, por favor introduzca el coste de los productos: ')

producto1 = float(input('Precio primer producto: '))
producto2 = float(input('Precio segundo producto: '))
producto3 = float(input('Precio tercer producto: '))

precio = producto1 + producto2 + producto3

if precio >= 50:
    descontado = precio -(precio * 0.15)
    precio = descontado +(descontado *0.21)
    print(f'Por su compra de {precio} euros(IVA incluido), usted obtiene un 15% de descuento dejando el precio en un total de {descontado} euros') 
elif precio >= 30 and precio < 50:
    precio = precio +(precio * 0.21)
    restante = 50 - precio
    print(f'Su compra es de {precio}, si gasta {restante} euros mas tendra acceso a un 15% de descuento ')
elif precio < 30:
    precio = precio +(precio * 0.21)
    print(f'Gracias por su compra de {precio}, esperemos que vuelva pronto')
else:
    print('No ha comprado nada')