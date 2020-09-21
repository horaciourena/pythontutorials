# # Ejecutar funciones dentro de otras funciones (Nested functions)
# def hello(nombre='Luis'):
#     print("La funcion hello() ha sido ejecutada!")

#     def saludar():
#         return '\t Esta es la funcion saludar() dentro de hello!'

#     def bienvenido():
#         return '\t Esta es la funcion bienvenido() dentro de hello!'
    
#     print(saludar())
#     print(bienvenido())
#     print("Este es el final de la funcion hello()")

# hello()
# # print(bienvenido()) // Funcion definida solo dentro del alcance de la funcion hello()


# # Retornar funciones dentro de otras funciones (Nested functions)
# def hello(nombre='Luis'):
#     print("La funcion hello() ha sido ejecutada!")

#     def saludar():
#         return '\t Esta es la funcion saludar() dentro de hello!'

#     def bienvenido():
#         return '\t Esta es la funcion bienvenido() dentro de hello!'

#     print("Voy a retornar una funcion!")

#     if nombre == 'Luis':
#         # return saludar() // Solo devolveria el string y necesitamos la funcion
#         return saludar
#     else:
#         # return bienvenido() // Solo devolveria el string y necesitamos la funcion
#         return bienvenido

# mi_funcion = hello('Luis')
# # print(mi_funcion)
# print(mi_funcion())