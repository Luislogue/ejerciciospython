import divisas
import primos
import palindromos



 


if __name__ == "__main__":
    eleccion = input("Por favor eliga que desea hacer"+"\n"
                        "divisas"+"\n"
                        "primos"+"\n"
                        "palindromos"+"\n")
    if eleccion == "divisas":
        divisas.menu()
    if eleccion == "primos":
        primos.datos()
    if eleccion == "palindromos":
        palindromos.pali()