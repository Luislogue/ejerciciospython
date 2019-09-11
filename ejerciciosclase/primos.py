'''
Numeros primos
Divisibles por 1 y ellos mismos
tabla de np empieza por 2
'''
def datos():
    numero = int(input("introduzca el numero que desea comprobar: "))
    
    print(primo(numero))

def primo(numero):
    
    if numero > 1:
        for i in range(2, numero):
            if(numero % i) == 0:
                return False  
            

        return True
   
if __name__ == "__main__":
    datos()


