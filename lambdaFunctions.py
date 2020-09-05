# # Funciones anonimas
# # Solo se ejecutan una unica vez
# # No poseen nombre

# # Map Function
# def potencia2(num):
#     return num**2
# nums = [1,2,3,4,5]

# for item in map(potencia2,nums):
#     print(item)

# print(list(map(potencia2,nums)))

# def separador(mystring):
#     if len(mystring)%2==0:
#         return 'Par'
#     else:
#         return mystring[0]

nombres = ['Sally', 'Carlos', 'Casey', 'Mercedes']
# print(list(map(separador,nombres)))

# # Filter Function

# def numPar(n):
#     return n%2==0

myNumbers = [1,2,3,4,5,6]

# print(list(filter(numPar,myNumbers)))
# for i in myNumbers:
#     print(i)

# Lambda Expresions

def potencia2(n):
    resultado = n**2
    return resultado

def potencia22(n):
    return n**2

def potencia23(n): return n**2

lambda n: n**2
potencia = lambda n: n**2
print(potencia(5))

print(list(map(lambda num: num**2,myNumbers)))
print(list(filter(lambda num: num%2==0,myNumbers)))
print(list(map(lambda name: name[0],nombres)))
print(list(map(lambda name: name[::-1],nombres)))