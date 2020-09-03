# *args y **kwargs

def suma(a,b):
    # Retorna el 5% de la suma de a + b
    return sum((a,b)) * 0.05

def suma2(*args):
    return sum(args) * 0.05

print(suma(40,60))
print(suma2(40,60,70,100))

def ejemplo2(**kwargs):
    if 'fruta' in kwargs:
        print('Poseo la fruta: {}.'.format(kwargs['fruta']))
    else:
        "Lo siente, no se encontro ninguna fruta."

def ejemplo3(**kwargs):
    print(kwargs)
    
ejemplo2(fruta = 'Naranja', vegetal = 'Lechuga')
ejemplo3(fruta = 'Naranja', vegetal = 'Lechuga')

def ej4(*args,**kwargs):
    print("Necesito {} {}.".format(args[0], kwargs['alimento']))
    print(kwargs)
    print(args)

ej4(10,15,20,fruta = 'Mango', alimento = 'Chuletas', animal = 'Alcon')