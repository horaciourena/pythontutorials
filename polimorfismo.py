# Polimorfismo
class Perro():
    def __init__(self,nombre):
        self.nombre = nombre
    def saludar(self):
        print(self.nombre + " te saluda.")

class Gato():
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        print(self.nombre + " te saluda.")

miPerro = Perro('Lola')
miGato = Gato('Froza')
# for mascota in [miGato,miPerro]:
#     print(type(mascota))
#     mascota.saludar()

# def saludar(mascota):
#     mascota.saludar()
#
# saludar(miPerro)
# saludar(miGato)

class Animal():
    def __init__(self, nombre):
        self.nombre = nombre
    def comer(self):
        raise NotImplementedError("La subclase debe implementar este metodo.")

class Pato(Animal):
    def comer(self):
        print(self.nombre + " esta comiendo.")

miPato = Pato('Carla')
miPato.comer()