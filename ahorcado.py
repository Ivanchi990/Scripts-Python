import os
import time
import getpass
import random

def borrarPantalla():
    time.sleep(1)
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")

vidas = 6

def verMuñeco():
    if vidas == 6:
        print("\n --------------|", "\n |             0  ", "\n |            \|/", "\n |             |  ","\n---           / \ ")

print("           /--------------------------------\ ")
print("            Bienvenido al ahorcado de PYTHON")
print("           \--------------------------------/ ")
print("-En el modo solitario se te generará una palabra aleatoriamente.")
print("-En el modo multijugador tu eligirás una palabra y el otro jugador tratará de adivinarla.")
print("-Tines una serie vidas, cada una de ellas será representada con el símbolo $.")
print("-Aviso, si en algun momento de la partida intentas adivinar la palabra y no es correcta habrás perdido. \nBuena suerte :)")

verMuñeco()
juego = int(input("1-Solitario \n2-Multijugador"))
while len(str(juego)) > 1 or str(juego).isalpha() == True:
    print("El caracter introducido no es válido, intentalo de nuevo: ")
    juego = int(input("1-Solitario \n2-Multijugador\n"))

if juego == 2:
    palabra = getpass.getpass("Introduce una palabra: \n")
    palabra.lower()
elif juego == 1:
    dificultad = 0
    dificultad = int(input("\n1-Fácil \n2-Dificil \n"))
    print("-Con el modo de juego fácil podras elegir un tema, por ejemplo animales, vehiculos ...")
    print("-Con el modo de juego dificil se generará de manera aleatoria una palabra de cualquier tema")
    while len(str(dificultad)) > 1 or str(dificultad).isalpha() == True:
        print("El caracter introducido no es válido, intentalo de nuevo: ")
        dificultad = int(input("1-Fácil \n2-Dificil \n"))
    if dificultad == 1:
        print("1-Animales \n2-Vehículos \n3-Ciudades/Capitales/etc \n4-Accidentes geograficos: \n")
        modo = int(input("Introduce la categoría que quieres: \n"))
        while len(str(modo)) > 1 or str(modo).isalpha() == True:
            print("El caracter introducido no es válido, intentalo de nuevo: ")
            modo = int(input("Introduce la categoría que quieres: \n"))
        if modo == 1:
            palabras = ["gato", "leon", "jirafa", "jaguar", "elefante", "araña", "murcielago", "perro", "raton", "guacamayo", "vaca", "oveja", "cordero", "gallina","delfin", "serpiente", "hamster", "cobaya", "caballo", "mono", "abeja", "mosca", "iguana", "hiena", "tortuga", "pez", "tiburon", "pajaro", "aguila", "paloma"]
        elif modo == 2:
            palabras = ["coche", "moto", "camion", "bicicleta", "patines", "monopatin", "patinete", "triciclo", "tren", "avion", "barco", "barca", "globo", "submarino", "yate", "uber", "taxi", "furgoneta"]
        elif modo == 3:
            palabras = ["Madrid", "España", "Colombia", "Zaragoza", "Rumania", "Lisboa", "Zamora", "Francia", "Paris", "Roma", "Italia", "Praga", "Rusia", "moscu", "galicia", "murcia", "chile", "argentina", "soria", "toledo", "chicago", "manhattan", "orlando", "mongolia", "bucarest", "sofia", "irlanda", "londres", "inglaterra", "india", "tokio", "china", "tailandia", "japon", "brasil", "valencia", "letonia", "estonia", "tallin", "lituania", "amdorra", "jaen", "cadiz", "pakistan", "turquia", "ankara", "malaga", "castellon", "arganda", "getafe", "leganes", "africa", "europa", "asia", "antartida", "lugo", "acoruña", "ourense", "pontevedra", "barcelona", "huesca", "albacete", "noruega", "bulgaria", "mentrida", "aliste", "santander", "cantabria", "asturias", "oviedo", "navarra", "vitoria", "menorca", "tenerife", "ceuta", "melilla"]
        elif modo == 4:
            palabras = ["aneto", "teide", "finisterre", "pirineos", "andes", "alpes", "nilo", "amazonas", "tajo", "miño", "cantabrico", "oceano", "rio", "montaña", "cordillera", "ladera", "meseta", "cabo", "golfo", "isla", "volcan", "archipielago"]
    elif dificultad == 2:
        palabras = ["aneto", "teide", "finisterre", "pirineos", "andes", "alpes", "nilo", "amazonas", "tajo", "miño", "cantabrico", "oceano", "rio", "montaña", "cordillera", "ladera", "meseta", "cabo", "golfo", "isla", "volcan", "archipielago", "coche", "casa", "hipopotamo", "cerveza", "edificio", "minotauro", "lego", "ordenador", "python", "ivan", "coche", "moto", "camion", "bicicleta", "patines", "monopatin", "patinete", "triciclo", "tren", "avion", "barco", "barca", "globo", "submarino", "yate", "uber", "taxi", "furgoneta", "vaca", "oveja", "cordero", "gallina", "defecar", "tenis", "metro", "tren", "raton", "gato", "leon", "jirafa", "jaguar", "elefante", "araña", "murcielago", "perro", "raton", "guacamayo", "delfin", "serpiente", "hamster", "cobaya", "caballo", "mono", "abeja", "mosca", "iguana", "hiena", "tortuga", "pez", "tiburon", "pajaro", "aguila", "paloma", "Madrid", "España", "Colombia", "Zaragoza", "Rumania", "Lisboa", "Zamora", "Francia", "Paris", "Roma", "Italia", "Praga", "Rusia", "moscu", "galicia", "murcia", "chile", "argentina", "soria", "toledo", "chicago", "manhattan", "orlando", "mongolia", "bucarest", "sofia", "irlanda", "londres", "inglaterra", "india", "tokio", "china", "tailandia", "japon", "brasil", "valencia", "letonia", "estonia", "tallin", "lituania", "amdorra", "jaen", "cadiz", "pakistan", "turquia", "ankara", "malaga", "castellon", "arganda", "getafe", "leganes", "africa", "europa", "asia", "antartida", "lugo", "acoruña", "ourense", "pontevedra", "barcelona", "huesca", "albacete", "noruega", "bulgaria", "mentrida", "aliste", "santander", "cantabria", "asturias", "oviedo", "navarra", "vitoria", "menorca", "tenerife", "ceuta", "melilla"]
    else:
        print("Opcion inválida, prueba de nuevo")
        print("-Con el modo de juego fácil podras elegir un tema, por ejemplo animales, vehiculos ...")
        print("-Con el modo de juego dificil se generará de manera aleatoria una palabra de cualquier tema")
        dificultad = int(input("1-Fácil \n2-Dificil \n"))

    numero = random.randint(0, len(palabras) - 1)
    palabra = palabras[numero]
    palabra.lower()
else:
    print("Opción no válida, intentalo de nuevo:\n")
    while len(str(juego)) > 1 or str(juego).isalpha() == True:
        juego = int(input("1-Solitario \n2-Multijugador \n"))
    
def verMuñeco():
    if vidas == 6:
        print("\n --------------|", "\n |             0  ", "\n |            \|/", "\n |             |  ","\n |            / \ ","\n |", "\n---")
    elif vidas == 5:
        print("\n --------------|", "\n |             0  ", "\n |            \|/", "\n |             |  ","\n |            /  ","\n |", "\n---")
    elif vidas == 4:
        print("\n --------------|", "\n |             0  ", "\n |            \|/", "\n |             |  ","\n |               ","\n |", "\n---")
    elif vidas == 3:
        print("\n --------------|", "\n |             0  ", "\n |            \|/", "\n |                ","\n |                ","\n |", "\n---")
    elif vidas == 2:
        print("\n --------------|", "\n |             0  ", "\n |            \|", "\n |                ","\n |                ","\n |", "\n---")
    elif vidas == 1:
        print("\n --------------|", "\n |             0  ", "\n |             |", "\n |                ","\n |                ","\n |", "\n---")
    elif vidas == 0:
        print("\n --------------|", "\n |             0  ", "\n |               ", "\n |                ","\n |                ","\n |", "\n---")

def verMenu():
    opcion = int(input("¿Que quieres hacer?: \n1-Probar con una letra \n2-Adivinar palabra completa:\n"))
    while len(str(opcion)) > 1 or str(opcion).isalpha() == True: 
        print("El caracter introducido no es válido, intentalo de nuevo: ")
        opcion = int(input("¿Que quieres hacer?: \n1-Probar con una letra \n2-Adivinar palabra completa:\n"))
    return opcion

print("Tienes :", vidas * "*", " vidas")
secreto = "*" * len(palabra)
secret = "-" * len(palabra)
letras = []

while vidas > 0:
    
    print("\nTienes :", vidas * "$ ")
    verMuñeco()
    print(secreto)
    print(secret)

    opcion = verMenu()
    while(opcion != 1 and opcion != 2):
        print("Opción no válida")
        opcion = verMenu()

    if opcion == 1:
        caracter = input("¿Que letra quieres introducir?\n")
        while caracter.isalpha() == False or caracter.isdigit() == True or len(caracter) > 1: 
            print("El caracter introducido no es válido")
            caracter = input("Intentalo de nuevo\n")
    elif opcion == 2:
        caracter = input("¿Que palabra quieres introducir?\n")
        
    caracter.lower()

    if len(caracter) == 1:
        for i in range(0, len(palabra)):
            if palabra[i] == caracter:
                secreto = secreto[0:i] + caracter + secreto[(i + 1):]
                print("El caracter", caracter," se encuentra en la palabra")
        if palabra.find(caracter) == -1:
            print("El caracter ", caracter," no se encuentra en la palabra")
            letras.append(caracter)
            vidas = vidas - 1
    else:
        if caracter == palabra:
            print("Enhorabuena has acertado la palabra :)")
            verMuñeco()
            vidas = 0
        else:
            print("Lo siento la palabra no es correcta, has perdido")
            vidas = 0
            verMuñeco()
    if secreto == palabra and len(caracter) == 1:
        print("Enhorabuena acertaste la palabra")
        vidas = 0
    
    if vidas == 0:
        print("La palabra era", palabra)
    
    print("Letras erradas")
    for j in letras:
        print(*j, end=", ")
    print("\n")
print("Fin del juego, gracias por jugar")