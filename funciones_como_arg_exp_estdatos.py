def multiplicar_por_dos(n):
    return n * 2

def sumar_dos(n):
    return n + 2

def aplicar_operaciones(f, numeros):
    resultados = []
    for numero in numeros:
        resultado = f(numero)
        resultados.append(resultado)

    return resultados

nums = [2,4,6]
print(aplicar_operaciones(multiplicar_por_dos, nums))
print(aplicar_operaciones(sumar_dos, nums))

# funciones como expresiones = lambda

sumar = lambda x, y: x + y
print(sumar(2, 3))

# funciones en estructuras de datos

def aplicar_operaciones(num):
    operaciones = [abs, float]

    resultado = []
    for operacion in operaciones:
        resultado.append(operacion(num))

    return resultado

print(aplicar_operaciones(-2))
