# Phone Number Checker
# Instagram Customer Service Number: +16505434800
# Altice Customer Service Number: +18098596555
import phonenumbers
from phonenumbers import carrier, geocoder

def numChecker(phoneNumber):
    info = []
    phone = phonenumbers.parse(phoneNumber)
    info.append(geocoder.description_for_number(phone,"es"))
    info.append(carrier.name_for_number(phone,"es"))
    return info

phoneNumber = input("Digite un numero de telefono: ")
print(numChecker(phoneNumber))