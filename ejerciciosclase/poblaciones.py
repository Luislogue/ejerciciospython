
def _get_poblaciones():
    return {
        'manacor':40000,
        'palma':500000,
        'calvia':15000,
        'llucmajor':20000,
        'inca':60000
    }  


def poblacion(pueblo):
    pueblo = pueblo.lower()
    poblaciones = _get_poblaciones()
    return(poblaciones.get(pueblo))
    
    
def limpiar():
    return _get_poblaciones().clear()
    
def insertar():
    insert_poblacion = input('Introduzca la nueva poblacion: ')
    insert_citizens = input('Introduzca el numero de ciudadanos: ')
    poblaciones = _get_poblaciones()
    poblaciones[insert_poblacion] = insert_citizens
    
    return poblaciones

if __name__ == "__main__":
    while True:
        user_input = input('Pulse \"s\" para salir, pulse \"x\" para borrar la lista, pulse \"v\" para ver lista o pulse \"i\" para introducir una nueva poblacion: ')
        if user_input == 's':
            break
        if user_input == 'v':
            print(_get_poblaciones())
        if user_input == 'x':
            print(limpiar())
        if user_input == 'i':
            while True:
                
                print(insertar())
                user_will = input('Pulse \"s\" para salir o continue introduciendo datos: ')
                continue


            

      