class Coche():

    # Estado inicial bajo constructor
    def __init__(self):
        self.__largoChasis = 300
        self.__anchoChasis = 160
        self.__ruedas = 4 #encapsular
        self.__enMarcha = False

    # METODO
       
    def __chequeoArranque(self):
        print('Estamos realizando el chequeo')

        self.gasolina = True
        self.aceite = True
        self.puertasCerradas = True
        self.bateria = True

        if(self.gasolina and self.aceite and self.puertasCerradas and self.bateria):
            return True
        else:
            return False

    def arrancar(self, arrancamos):
        self.enMarcha = arrancamos

        if(self.enMarcha):
            chequeo = self.__chequeoArranque()

        # if(self.arrancar)
        #     return 'El coche esta en marcha'
        # else:
        #     return 'El coche esta apagado'

        if(self.enMarcha and chequeo):
            return 'El coche esta en marcha'
        elif(self.enMarcha and chequeo == False):
            return '`Problemas al arracar'
        else:
            return 'El coche esta parado'
     


    def estado(self):
        print(f'El coche tiene {self.__ruedas} ruedas, un ancho de {self.__anchoChasis} y una longitud de {self.__largoChasis}')
     


    # INSTANCIAR UNA CLASE, CREAR UN OBJETO
    # NO SE USA NEW

miCoche = Coche()

    # Acceder a las propiedades

print(miCoche.arrancar(True))

    # Acceder a los metodos

miCoche.estado()

print('--------------------------Segunda Instancia/Objeto---------------------------')

cocheDelVecino = Coche()
print(cocheDelVecino.arrancar(False))
cocheDelVecino.estado()
print('--------------------------Tercera Instancia/Objeto---------------------------')

cocheDelAbuelo = Coche()
print(cocheDelAbuelo.arrancar(False))
cocheDelAbuelo.estado()

