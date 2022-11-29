from io import open

archivo_texto=open("archivo.txt", "w") ## Escritura
frase="Cuando cuentes cuentos \n cuenta cuantos cuentos cuentas"
archivo_texto.write(frase)
archivo_texto=open("archivo.txt", "a") ## Append
archivo_texto.write("Tres tristes tigres tragaban trigo en un trigal")
archivo_texto=open("archivo.txt", "r+") ## Lectura (+ y escritura)
informacion=archivo_texto.read("""Se Puede pasar un argumento de hasta que numero de caracter se quiere leer""")
archivo_texto.seek(0)
lista_lineas=archivo_texto.readlines()
archivo_texto.close()
print(lista_lineas[0]) ## Puntero en texto
print(informacion)
archivo_texto.writelines("""Se ingresa una lista como argumentos""")