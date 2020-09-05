# class Ejemplo():
#     pass
# miEjemplo = Ejemplo()
# print(type(miEjemplo))

class Perro():

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

# miPerro = Perro('Dalmata')
# miPerro = Perro('Dalmata','Pop',True)
# print(type(miPerro))
# print(miPerro.raza)
# print(miPerro.nombre)
# print(miPerro.vacunas)

miPerro = Perro()
miPerro.raza = "Dalmata"
miPerro.nombre = "Lola"
miPerro.vacunas = "True"

print(miPerro.raza)
print(miPerro.nombre)
print(miPerro.vacunas)