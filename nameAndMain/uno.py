# uno.py

# if __name__ == "__main__":
# identacion Nivel Cero // No main() function

# Lo que sucede al ejecutar el script por consola
# __name__ = '__main__'

def funcion():
    print("Funcion en uno.py")

print("Nivel Cero en uno.py")

if __name__ == '__main__':
    print("uno.py esta siendo ejecutado directamente!")
else:
    print('uno.py ha sido importado.')