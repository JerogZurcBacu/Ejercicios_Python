# La recursividad programática se trata de una función que se llama a si misma

def factorial(n):
    """Calcula el factoriqal de n

    n int > 0
    return n!
    """
    if n == 1:
        return 1

    return n * factorial(n-1)

n = int(input('Escribe un número entero: '))

print(factorial(n))