x = 0
while x < 5:
    print(f'El valor actual de x es {x}.')
    x += 1
else:
    print(f'Ahora x es igual a {x}.')

x = 55
while x < 5:
    print(f'El valor actual de x es {x}.')
    x += 1
else:
    print(f'Ahora x es igual a {x}.')

# brake, continue, and Pass

x = [1,2,3]

for item in x:
    # this is just a comment
    pass
print("Comentario de prueba!")

formatos = "M.e.r.cede.s"
for letra in formatos:
    if(letra=='.'):
        continue
    print(letra)

num = [2,4,6,7,8,10,11,13,14]
num2 = [2,4,6,8,10,14]
for n in num2:
    if(n%2!=0):
        print(f"El primer numero impar es: {n}")
        break
else:
    print("Esta lista no posee numeros impares.")