# from raza_paises import paises
def seleccionar_raza():
    españa = {'ratero', 'galgo', 'politico'}
    ingles = {'bulldog', 'bullTerrier', 'beagle'}
    frances = {'bulldogFrances', 'DogoDBurdeos', 'Papillon'}


    selection = input('''De que pais desea conocer las razas:
    
        1-España
        2-Inglaterra
        3-Francia

     ''')
    selection = selection.lower()
    if selection == "1" or selection == "españa":
        return españa
    
    if selection == "2" or selection == "inglaterra":
        return ingles
    
    if selection == "3" or selection == "francia":
        return frances
        
