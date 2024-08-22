#!/usr/bin/env python3

# Programa que valida si una palabra o frase es un palíndromo (que se lee igual en un sentido que en otro).
# miFuncion("salas") devolverá true

def palindromo(palabra):
    palabra = palabra.replace(" ", "").lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False



def run():
    try:
        palabra = input("Ingresa una palabra: ")
        if palindromo(palabra):
            print("Es palindromo")
        else:
            print("No es palindromo")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    run()