objetivo = int(input('Elije un número: '))

epsilon = 0.001
paso = epsilon**2
respuesta = 0

while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
    respuesta += paso

if abs(respuesta**2 - objetivo) >= epsilon:
    print(f'no se encontro la raiz cuadrada de {objetivo}')
else:
    print(f'La raiz cuadrada de {objetivo} es {respuesta}')