# def crear_cubos(n):
#     resultado = []
#     for i in range(n):
#         resultado.append(i**3)
#     return resultado

# print(crear_cubos(10))
# for i in crear_cubos(10):
#     print(i)

# def crear_cubos(n):
#     for i in range(n):
#         yield i**3

# for i in crear_cubos(10):
#     print(i)

# print(crear_cubos(10))
# print(list(crear_cubos(10)))

# def gen_fubon(n):
#     a,b = 1,1
#     for i in range(n):
#         yield a
#         a,b = b, a+b
    
# def gen_fubon2(n):
#     a,b = 1,1
#     resultado = []
#     for i in range(n):
#         resultado.append(a)
#         a,b = b, a+b
#     return resultado

# for number in gen_fubon(10):
#     print(number)

# print(list(gen_fubon(10)))

# for number in gen_fubon2(10):
#     print(number)

# print(list(gen_fubon2(10)))

# def simple_gen():
#     for i in range(3):
#         yield i

# for number in simple_gen():
#     print(number)

# g = simple_gen()
# print(g)
# print(next(g))
# print("Diferente linea de codigo ejecutada!")
# print(next(g))
# print(next(g))
# print(next(g))

s = 'Hola'
# for letra in s:
#     print(letra)

# next(s)

s_iter = iter(s)
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))