# Tuplas

def coordenadas():
    return(5, 4)

print(coordenadas()) # (5, 4) es una tupla de dos elementos

x, y = coordenadas()
print(x)
print(y)

# Rangos

my_range = range(0,10,2)
#my_range es un rango del 0 al 9 (el ultimo digito no se invluye), con saltos de dos en dos

for i in my_range:
    print(i)

# Litas y mutabilidad

my_list = [1, 2, 3]

#Acceso mediante indices
print(my_list[0])

#Notacion de sliders
print(my_list[1:])

#Modificar mediante Indice
my_list[1] = "a"
print(my_list)

#Agregar elemento a lista - Append
my_list.append(4)
print(my_list)

#Borrar elemento a lista - Pop
my_list.pop()
print(my_list)

#Mutar lista
a = [1, 2, 4]
b = a
a.append(8)
print(a)
print(b)

#Clonar lista
c = [1, 2, 4]
d = list(c)
c.append(8)
print(c)
print(d)

#List comprehension
#Es una forma concisa de aplicar operaciones a los valores de una secuencia. Tambien se pueden aplicar condiciones para filtrar.

my_list2 = list(range(10))
print(my_list2)

#Multiplicar por 2 cada elemento de la lista
double = [i * 2 for i in my_list2]
print(double)

#Filtrar numeros pares
filtro_par = [i for i in my_list2 if i % 2 == 0]
print(filtro_par)

#Diccionarios
my_dic = {
    'nombre': 'Jorge',
    'apellido': 'Cruz',
    'edad': 28
}

print(my_dic)

#Acceso a diccionario
print(my_dic['nombre'])

#Valores predeterminados
print(my_dic.get('email', 'jorgecruzprof@gmail'))
print(my_dic.get('apellido', 'jorgecruzprof@gmail'))

#Reasignacion de valor
my_dic['edad'] = 30
print(my_dic['edad'])

#Eliminar elemento
del my_dic['edad']
print(my_dic)

#Imprimir llaves o valores y ambos
for llave in my_dic.keys():
    print(llave)

for valor in my_dic.values():
    print(valor)

for llave, valor in my_dic.items():
    print(llave, valor)

#Reviar si llave existe en diccionario
'email' in my_dic
'nombre' in my_dic

