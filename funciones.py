def saludar():
    print("Hola a todos!")

def saludar2(nombre):
    print(f'Hola {nombre}.')

saludar()
saludar2('Horacio')

#####################################################

def sumar(a,b):
    return a + b

# Ver diferencias entre Print y Return en funciones

# Verificar la data que estamos pasando a las funciones

print(sumar(15,7))
print(sumar('15','7'))
print(sumar(15,'7'))

# Implementado Logica a las Funciones

def numeroPar(num):
    if(num%2==0):
        return True
    else:
        return False

def numeroPar2(num):
    resultado = num%2==0
    return resultado

def numeroPar3(num):
    return num%2==0

def numeroParLista(lista):
    for num in lista:
        if num%2==0:
            # return num
            return True
    else:
        return False

def numeroParLista2(lista):
    pares = []
    for num in lista:
        if num%2==0:
            pares.append(num)
    if(len(pares)>0):
        return pares
    else:
        return False

print(numeroParLista([1,3,5]))
print(numeroParLista([1,2,3,4,5]))
print(numeroParLista2([1,2,3,4,5]))
print(numeroParLista2([1,3,5]))

# Unpacking Tuplas con Funciones
def empleadoMes(a):
    maxHoras = 0
    empleadoDelMes = ''

    for empleado, horas in a:
        if horas > maxHoras:
            maxHoras = horas
            empleadoDelMes = empleado

    return (empleadoDelMes,maxHoras)
    # return f'El empleado del mes es: {empleadoDelMes} con {maxHoras} horas trabajadas.'

listaEmpleados = [('Luis',100),('Martha',400),('Lucas',800)]
print(empleadoMes(listaEmpleados))
name, hours = empleadoMes(listaEmpleados)
print(name)
print(hours)