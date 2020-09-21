# # Recibir funciones como parametros dentro de otras funciones
# def hello():
#     return 'Hola Luis!'

# def other(otra_funcion):
#     print("Otro codigo se ejecuta aqui.")
#     print(otra_funcion())

# other(hello)

# Finally Decoradores!!!! :)
def decorador(funcion_original):

    def funcionalidad_extra():
        print("Codigo extra, antes de la funcion original")
    
        funcion_original()

        print("Codigo extra, luego de la funcion original")

    return funcionalidad_extra

# def necesito_ser_decorada():
#     print("Quiero ser decorada!!")

# necesito_ser_decorada()
# funcion_decorada = decorador(necesito_ser_decorada) # Sintaxis especial para esta linea con el operador @
# funcion_decorada()

@decorador
def necesito_ser_decorada():
    print("Quiero ser decorada!!")

necesito_ser_decorada()