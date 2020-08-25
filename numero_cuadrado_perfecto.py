from math import sqrt

num = int(input("Digite un numero: "))
# print(f'La raiz cuadrada de {num} es: {sqrt(num)}')
# print(f'La raiz cuadrada ENTERA de {num} es: {int(sqrt(num))}')
if( (int(sqrt(num)) * int(sqrt(num))) == num ):
    print(f'El numero: {num} es cuadrado perfecto!')
else:
    print(f'El numero: {num} NO es cuadrado perfecto!')