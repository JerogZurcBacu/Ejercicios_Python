## try, except, finally...

print("Calculadora de divisiones")

while True:
    try:
        op1 = (int(input("Introduce el primer número: ")))
        op2 = (int(input("Introduce el segundo número: ")))
        break
    except ValueError:
        print("Los valores introducidos no sen correctos, intentalo de nuevo")

def divide_uno(num1, num2):
    try:
        return num1/num2
    except ZeroDivisionError:
        print("No se puede dividir entre 0")
        return "Operación errónea"
##print(divide_uno(op1,op2))
##print("Programa terminado")

def divide_dos():
    try:
        print("La división es: " + str(op1/op2))
    except ValueError:
        print("El valor introducido es erroneo")
    except ZeroDivisionError:
        print("No se puede dividir entre 0!")
    finally:
        print("Calculo finalizado")

divide_dos()