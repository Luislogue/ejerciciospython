import random
import os

'''
    *---*
    |   |
    o   |
   /|\  |
    |   |
   / \  |
        *========*



'''

def adivinanza():
    os.system('clear')
    barras = "-"*len(palabraSecreta)
    intentos = 7

    while intentos > -1 and not barras == palabraSecreta:
        print(barras)
        print(str(f'Tienes {intentos} intentos'))

        adivina = (input("Adivina: "))

        if len(adivina) != 1:
            print("Por favor introduzca solo un caracter")
        if adivina in palabraSecreta:
            print("Has acertado")
            barras = update_barras(palabraSecreta, barras, intentos)
        else:
            print("Te equivocaste")
            intentos -= 1
    if intentos <= 0:
        print(f'Has perdido, la palabra era {palabraSecreta}')   
    else:
        print(f'Has ganado, la palabra es {palabraSecreta}')         


def update_barras(palabraSecreta, barras, adivina):
  resultado = ""
  
  for i in range(len(palabraSecreta)):
    if palabraSecreta[i] == adivina:
      resultado = resultado + adivina     
      
    else:
 
      resultado = resultado + barras[i]
      
  return resultado
    
palabras = ["bob", "cool", "whatup"]

palabraSecreta = random.choice(palabras)
adivinanza()


if __name__ == "__main__":
    adivinanza()