import string
import time
import random

def fuerza_bruta(target):
    caracteres = string.ascii_lowercase + string.ascii_uppercase + ' ' + string.punctuation
    generada = [''] * len(target)

    for i in range(len(target)):
        while True:
            c = random.choice(caracteres)
            generada[i] = c
            print(''.join(generada))
            time.sleep(0.05)  # Añade un retardo de 0.05 segundos
            if c == target[i]:
                break

fuerza_bruta('Hola Mundo!!')
