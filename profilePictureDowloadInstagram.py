import instaloader

def pictureDownloader(userName):
    parser = instaloader.Instaloader()
    # parser.download_profile(userName,profile_pic_only=True)
    # parser.download_profile(userName,profile_pic=True)

userName = input("Digite el nombre de usuario de Instagram: ")
print("Descargando...")
pictureDownloader(userName)
print("Descarga Completa!")