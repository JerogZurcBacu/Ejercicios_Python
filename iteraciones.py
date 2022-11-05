contador = 0

while contador < 10:
    print(contador)
    contador += 1

    if contador > 6:
        break

frutas = ["manzana", "pera", "mango"]

for fruta in frutas:
    print(fruta)

estudiantes = {
    "mexico": 10,
    "colombia": 15,
    "puerto_rico": 4, 
}

for pais in estudiantes:
    print(pais)

for pais in estudiantes.keys():
    print(pais)

for pais in estudiantes.values():
    print(pais)

for pais in estudiantes.items():
    print(pais)