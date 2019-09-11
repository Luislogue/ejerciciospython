'''

Decoradores
Funciones que a su vez añaden funcionalidades en otras funciones

Estructura:
3 Funciones(a b y c) donde a recibe como parametro a b para devolver c

Un decorador se aplica a una funcion o metodo con el simbolo @

Los decoradores es codigo muy habitual en python y en sus frameworks


'''
# Una funcion que recibe a una funcion
def proteger(func):


    # Encapsular dentro proteger
    def envolver(password):
        if password == 'muevete':
            return func()
               
        else:
            print('Contraseña incorrecta')
                
    return envolver
@proteger
def proteger_login():
    print('Tu contraseña es correcta')

if __name__ == "__main__":
    password = input('Por favor introduzca la contraseña: ')

    proteger_login(password)
# Pypi(python package nodes)
# 
# 