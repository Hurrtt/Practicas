import random
import string

def eleccion():
    letras = string.ascii_letters
    digitos = string.digits
    caracteres_especiales = string.punctuation
    diccrionario = ''
    logitud = int(input("Elija la longitud de su contraseña: "))
    aggLetras = input("¿Desea usar letras en su codigo? s-Sí o n-No: ")
    aggDigitos = input("¿Desea usar digitos en su codigo? s-Sí o n-No: ")
    aggCaracsEspeciales = input("¿Desea usar Caracteres en su codigo? s-Sí o n-No: ")
    if aggLetras == "s":
        diccrionario += letras
    if aggDigitos == "s":
        diccrionario += digitos * 2
    if aggCaracsEspeciales == "s":
        diccrionario += caracteres_especiales
    else:
        print("")
    
    print(diccrionario)

    contraseña = ''.join(random.choice(diccrionario)  for _ in range(logitud))
    return contraseña


print("La contraseña es:" , eleccion())
