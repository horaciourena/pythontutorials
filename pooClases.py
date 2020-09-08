# class Ejemplo():
#     pass
# miEjemplo = Ejemplo()
# print(type(miEjemplo))

# class Perro():

#     # def __init__(self,raza,nombre,vacunas):
#     #     # Atributos
#     #     self.raza = raza
#     #     self.nombre = nombre
#     #     self.vacunas = vacunas
    
#     def __init__(self):
#         # Atributos
#         self.raza = ''
#         self.nombre = ''
#         self.vacunas = ''

# # miPerro = Perro('Dalmata')
# # miPerro = Perro('Dalmata','Pop',True)
# # print(type(miPerro))
# print(miPerro.raza)
# print(miPerro.nombre)
# print(miPerro.vacunas)

# miPerro = Perro()
# miPerro.raza = "Dalmata"
# miPerro.nombre = "Lola"
# miPerro.vacunas = "True"

# print(miPerro.raza)
# print(miPerro.nombre)
# print(miPerro.vacunas)

# Metodos y Atributos de Clase

class Perro():

    # Class Object Attribute
    # Same for any instance of a Class
    especie = 'Mamifero'

    # def __init__(self,raza,nombre,vacunas):
    #     # Atributos
    #     self.raza = raza
    #     self.nombre = nombre
    #     self.vacunas = vacunas
    
    def __init__(self):
        # Atributos
        self.raza = ''
        self.nombre = ''
        self.vacunas = ''
    
    # Operaciones / Acciones ===> Methods / Metodos

    def ladrar(self):
        print("WOOF!")

    def ladrar2(self):
        print("WOOF! Mi nombre es: {}".format(self.nombre))

    def ladrar3(self, edad):
        print("WOOF! Mi nombre es: {} y mi edad es: {}".format(self.nombre, edad))

class Circulo():
        # Class Object Attribute
    pi = 3.14

    def __init__(self,radio=1):
        self.radio = radio
        self.area = (radio**2) * self.pi
        # self.area = (radio**2) * Circulo.pi

    # Metodo
    def getCircunferencia(self):
        return self.radio * self.pi * 2
        # return self.radio * Circulo.pi * 2

miCirculo = Circulo(15)
print(miCirculo.radio)
print(miCirculo.getCircunferencia())
print(miCirculo.area)