import random
import string

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

    letras_por_adivinar = set(palabra)
    letras_adivinadas = set()
    abc = set(string.ascii_uppercase)

    vidas = 7
