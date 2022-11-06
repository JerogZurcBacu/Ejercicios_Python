# def nombre(parametros):
#     cuerpo
#     return expresion

def suma(a, b):
    resultado = a + b
    return print(resultado)

suma(2, 3)

def nombre_completo(nombre, apellido, inverso=False):
    if inverso:
        return print(f'{apellido} {nombre}')
    else:
        return print(f'{nombre} {apellido}')

nombre_completo('Jorge', 'Cruz')
nombre_completo('Jorge', 'Cruz', inverso=True)
nombre_completo(apellido='Cruz', nombre='Jorge')

#comentario de linea

"""Especificaciones del código

   - Que hace la instrucción
   - Que significan los parametros
   - Que es lo que devuelve nuestra instrucción 
"""


