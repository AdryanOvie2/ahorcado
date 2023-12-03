import random
import string

from palabras import palabras
from diagrama import vidas_diccionario_visual


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

    while len(letras_por_adivinar) > 0 and vidas > 0:
        print(f"Te quedan {vidas} vida(s) y has usado estas letras: {' '.join(letras_adivinadas)}")

        palabra_lista = [letra if letra in letras_adivinadas else '-' for letra in palabra]
        print(vidas_diccionario_visual[vidas])
        print(f"Palabra: {' '.join(palabra_lista)}")

        letra_usuario = input("Escoge una letra: ").upper()

        if letra_usuario in abc - letras_adivinadas:
            letras_adivinadas.add(letra_usuario)

            if letra_usuario in letras_por_adivinar:
                letras_por_adivinar.remove(letra_usuario)
                print('')
            else:
                vidas -= 1
                print(f"\nTu letra, {letra_usuario} no está en la palabra.")
        elif letra_usuario in letra_usuario:
            print("\nYa escogiste esa letra. Por favor escoge una letra nueva.\n")
        else:
            print("\nEsta letra no es válida.")

    if vidas == 0:
        print(vidas_diccionario_visual[vidas])
        print(f"\n¡Ahorcad@! Perdiste. Lo siento mucho. La palabra era {palabra}")
    else:
        print(f"¡Excelente! ¡Adivinaste la palabra {palabra}!")


ahorcado()