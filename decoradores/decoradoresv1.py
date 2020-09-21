# def func():
#     return 21

# print(func())
# print(func)

def hello():
    return "Hello!"

# print(hello())
# print(hello)

# saludar = hello() // Solo asigna el string que devuelve la funcion hello()
saludar = hello
print(saludar())

del hello
# print(hello())
print(saludar())