#!/usr/bin/env python3

# Programa una funcion que obtenga un numero aleatorio entre 501 y 600


import random


def numero_random():
    return random.randint(500,600)

for i in range(10):
    print(numero_random())