import random

class Lampara():
    # from asciiart import _LAMPARA
    # asciiart.lampara
    
    def __init__(self):
        self.__encendido = False

    def encender(self):
        if self.__encendido == True:
            return 'La lampara ya esta encendida'
        else:
            self.__encendido = True
            return 'La lampara se ha encendido'
      
    def apagar(self):
        if self.__encendido == False:
            return 'La lampara ya esta apagada'
        else:
            self.__encendido = False
            return 'La lampara se ha apagado'
      


if __name__ == "__main__":
    miLampara = Lampara()
    print(miLampara.encender())
    contador = 0
    random_number = random.randint(0,8)
    print(random_number)
    while contador < random_number:
        opcion = input('Quieres encender la lampara? Pulsa \"1\" para encender o \"2\" para mantenerla apagada o la \"s\" para salir: ')   
        if opcion == 's':
            break
        if opcion == '1':
            print(miLampara.encender())
            contador = contador + 1
            
        if opcion == '2':
            print(miLampara.apagar())
            contador = contador + 1
        if contador == random_number:
            print('Has petao la bombilla retrasao')
            break