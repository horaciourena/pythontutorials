mi_lista = [1,2,3]

# Range() function
for num in range(10):
    print(num)

for num in range(1,10):
    print(num)

for num in range(0,10,2):
    print(num)

# Esta funcion es muy comunmente utilizada como un generador de valores.

print(range(0,11,2))
print(list(range(0,11,2)))

contador_indices = 0
palabra = 'abcdefg'

for letra in 'abcdefg':
    print(f'La letra {letra} se encuentra en el indice {contador_indices}.')
    contador_indices += 1

for letra in palabra:
    print(palabra[contador_indices])
    contador_indices += 1

ENUMARATE
for item in enumerate(palabra):
    print(item)

for indice,letra in enumerate(palabra):
    print(f'La letra {letra} se encuentra en el indice {indice}.')



# zip() function
lista1 = [1,2,3,4,5]
lista2 = ['a','b','c','e','f']
lista3 = [100,200,300]
# print(zip(lista1,lista2))

for item in zip(lista1,lista2):
    print(item) # Ahora podemos imprimir ambas listas en formato de tuplas

for item in zip(lista1,lista2,lista3):
    print(item) # Ahora podemos imprimir las tres listas en formato de tuplas

lista1 = [1,2,3,4,5,6,7,8,9,10]
for item in zip(lista1,lista2,lista3):
    print(item) # Ahora podemos imprimir las tres listas en formato de tuplas

print(list(zip(lista1,lista2)))
print(list(zip(lista1,lista2,lista3)))

# IN Operator

print('x' in [1,2,3]) # Listas numericas
print('x' in ['x','y','z']) # Listas de caracteres o Strings
print('av' in "avion") # Strings
dic = {'k1': 234, 'k2': 421}
print('k1' in dic) # Diccionarios
print(234 in dic.values()) # Diccionarios

# min() y max() funcions

lista = [11,23,45,78,106]
print(min(lista))
print(max(lista))

from random import shuffle, randint

my_list = [1,2,3,4,5,6,7,8,9,10]
print(my_list)
shuffle(my_list)
print(my_list)
print(randint(0,100))