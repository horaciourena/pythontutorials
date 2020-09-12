a = int(input("Primer Numero: "))
b = int(input("Segundo Numero: "))
c = int(input("Tercer Numero: "))
mayor = a
if b > a and b > c:
    mayor = b
elif c > a and c > b:
    mayor = c

print("El mayor de los tres numeros es:", mayor)
