#!/usr/bin/env python3

# Programa una funcion que cuente el numero de caracteres de una cadena de texto. 
# miFuncion("Hola mundo") devolvera 10

def contar_caracteres(cadena=""):
    if not cadena:
        print("No ingresaste ninguna cadena")
    else:
        print(f'La cadena "{cadena}" tiene {len(cadena)} caracteres')

# Ejemplos de uso
contar_caracteres()
contar_caracteres("Hola mundo")