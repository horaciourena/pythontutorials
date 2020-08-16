mi_lista = [1,2,3,4,5,6,7,8,9,10]
for elemento in mi_lista:
    print(elemento)

for elemento in mi_lista:
    print("Soy un ejemplo")

for num in mi_lista:
    if(num % 2 == 0):
        print(num)

for num in mi_lista:
    if(num % 2 == 0):
        print(num, "Es Par.")
    else:
        print(num, "Es Impar.")

suma_de_elementos = 0
for num in mi_lista:
    suma_de_elementos += num
print(suma_de_elementos)

suma_de_elementos = 0
for num in mi_lista:
    suma_de_elementos += num
    print(suma_de_elementos)

mi_string = "Hola Mundo!!"
for letra in mi_string:
    print(letra)

mi_string = "Hola Mundo!!"
for _ in mi_string:
    print("Nice!")

mi_tupla = (1,2,3)
for item in mi_tupla:
    print(item)

#Tuple Packing and Unpacking

new_list = [(1,2),(3,4),(5,6),(7,8)]
for item in new_list:
    print(item)

new_list = [(1,2),(3,4),(5,6),(7,8)]
for (a,b) in new_list:
    print(a)
    print(b)

new_list = [(1,2),(3,4),(5,6),(7,8)]
for a,b in new_list:
    print(b)

mi_diccionario = {'k1':1, 'k2':2, 'k3': 3}
for item in mi_diccionario:
    print(item)

mi_diccionario = {'k1':1, 'k2':2, 'k3': 3}
for item in mi_diccionario.values():
    print(item)

mi_diccionario = {'k1':1, 'k2':2, 'k3': 3}
for (llave,valor) in mi_diccionario:
    print(valor)