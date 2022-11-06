objetivo = int(input('Escuje un número entero: '))

resultado = 0

while resultado**2 < objetivo:
    resultado += 1

if resultado**2 == objetivo:
    print(f'La raíz cuadrada de {objetivo} es {resultado}')
else:
    print(f'El número {objetivo} no tiene raíz cuadrada exacta')