#!/usr/bin/env python3

# Programa una funcion que reciba un numero y evalue si es capicua o no (que se lee igual
# en un sentido que en otro. ejemplo. miFuncion(2002) devolvera true)

def capicua(numero):
    if not numero:
        raise ValueError("Debes ingresar un número")
    
    if not isinstance(numero, int):
        raise ValueError("Debes ingresar un número válido.")

    numero_str = str(numero)
    numero_al_reves = numero_str[::-1]
    return int(numero_str) == int(numero_al_reves)

def run():
    try:
        resultado = capicua(987)
        print(resultado)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    run()