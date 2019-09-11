import math

# Question 2
# Level 1

# Question:
# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

def fact():
    if numero == 0:
        return 'No es un numero valido'
    
    return math.factorial(numero)
if __name__ == "__main__":
    numero = int(input('Por favor introduzca el numero a factorizar: '))
    print(f'el resultado es: {fact()}')