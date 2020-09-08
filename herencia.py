# Herencia

# Clase Base // Base Class
class Animal():
    def __init__(self):
        print("Animal creado.")

    # def __init__(self, estado = 'Animal creado.'):
    #     # print("Animal creado.")
    #     self.estado = estado

    def quienSoy(self):
        print("Soy un animal.")

    def comer(self):
        print("Estoy comiendo.")

# Clase Derivada
class Perro(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Perro creado.")
    
    # def quienSoy(self):
    #     print("Soy un perro.")

    def ladrar(self):
        print("WOOF!")

# miAnimal = Animal()
# print(miAnimal)
# print(miAnimal.quienSoy())
# print(miAnimal.comer())

miPerro = Perro()
# miPerro.comer()
# miPerro.quienSoy()
# miPerro.ladrar()