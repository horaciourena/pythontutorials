from __future__ import unicode_literals
import youtube_dl

options = {
    'verbose': True,
    'fixup': 'detect_or_warn',
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '1411',
    }],
    'extractaudio': True,
    'outtmpl': r"C:\\Users\\luis\\Documents\\pythontutorials" + '/%(title)s.%(ext)s',
    'noplaylist': True
}

ydl = youtube_dl.YoutubeDL(options)
url = input("Digite la URL: ")
print("Descargando...")
ydl.download(url)
print("Descarga Finalizada!")