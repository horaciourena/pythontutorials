import requests
from random import randint

url = 'https://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain'
datos = requests.get(url)
texto = datos.text
#print(texto)
palabras = texto.split()
#print(palabras)
num_aleatorio = randint(0,len(palabras))
print(palabras[num_aleatorio]+str(num_aleatorio))