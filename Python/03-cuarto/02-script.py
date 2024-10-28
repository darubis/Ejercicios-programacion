#!/usr/bin/env python3

# Programa una funcion que determine si un numero es par o impar. miFuncion(29)
# devolvera Impar

def es_par(numero):
    if numero % 2 == 0:
        return True
    return False

def main():
    numero = input("Ingresa un numero => ")
    assert numero.isnumeric(), "Debes ingresar un numero"
    numero = int(numero)  # Convertir la entrada a un entero
    if es_par(numero):
        print("Es par")
    else:
        print("Es impar")

if __name__ == '__main__':
    main()