import io
import pygame
from gtts import gTTS

text = input("Digite el texto a reproducir: ")
print("Convirtiendo el texto a Audio, muy pronto iniciara la reproduccion del mismo...")
with io.BytesIO() as file:
    # gTTS(text=text, lang="en").write_to_fp(file)
    gTTS(text=text, lang="es").write_to_fp(file)
    file.seek(0)
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue
print("Reproduccion finalizada!")