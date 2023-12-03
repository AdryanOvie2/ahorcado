import random

from palabras import palabras


def obtener_palabra_valida(palabras):
    palabra = random.choice(palabras)

    while "-" in palabra or " " in palabra:
        palabra.random.choice(palabras)
    
    return palabra.upper()


def ahorcado():
    print("============================================")
    print("===========Bienvenido al Ahorcado===========")
    print("============================================")

    palabra = obtener_palabra_valida(palabras)
