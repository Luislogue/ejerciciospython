# Question 5
# Level 1

# Question:
# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.

# Hints:
# Use __init__ method to construct some parameters
class Dos_metodos():
    

    def __init__(self):
        self.__frase = ""
        
    def get_string(self):
        self.__frase = input("Introduza la frase: ")
    def printString(self):
        print(self.__frase.upper())
if __name__ == "__main__":
    
    miFrase = Dos_metodos()
    miFrase.get_string()
    miFrase.printString()

        

