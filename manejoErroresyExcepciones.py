# def sumar(a,b):
#     print(a+b)

# # sumar(10,20)
# n1 = 10
# n2 = input("Digite un numero: ")
# # sumar(n1,n2)
# # print("Script ejecutado completamente!")

# try:
#     sumar(n1,20)
# except:
#     print("Ha ocurrido un error, favor verifique los valores que intenta sumar.")
# else:
#     print("Script ejecutado completamente!")

# try:
#     f = open('prueba','r')
#     f.write('Linea de prueba')
# except TypeError:
#     print("Ha ocurrido un TypeError!")
# # except OSError:
# #     print("Ha ocurrido un OSError!")
# except:
#     print("Todas las demas excepciones")
# finally:
#     print("Yo siempre me ejecuto!")

# def validarNumEntero():
#     while True:
#         try:
#             n = int(input("Digite un numero: "))
#         except:
#             print("Lo sentimos, el valor digitado no es un numero entero.")
#             continue
#         else:
#             print("Entero validado, gracias!")
#             break
#         finally:
#             print("Final de mi Try/Except/Finally")
#             print("Yo siempre me ejecuto :)")

# validarNumEntero()