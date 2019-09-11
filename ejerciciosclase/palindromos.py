'''
PALINDROMO

'''

def pali():
    palabra  = str(input("Por favor introduzca el palabra: "))

    print(f'es la palabra: {palabra} un palindromo? {comprobar(palabra)}')
def comprobar(palabra):
    reversed = palabra[::-1]
    if reversed == palabra:
        return True
    else:
        return False


if __name__ == "__main__":
    pali()