from pytube import YouTube

url = input("Introduzca la URL del Video: ")
print("Descargando...")
# YouTube(url).streams.get_by_resolution()
# YouTube(url).streams.first().download()
YouTube(url).streams.get_highest_resolution().download()
print("Su video se ha descargado satisfactoriamente!")