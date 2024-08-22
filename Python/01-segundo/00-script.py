#!/usr/bin/env python3

def invertir_cadena(cadena: str) -> str:
    """Invierte las palabras de una cadena de texto.

    Args:
        cadena (str): La cadena de texto a invertir.

    Returns:
        str: La cadena de texto invertida.

    Raises:
        ValueError: Si el argumento no es una cadena válida.
    """
    if not cadena:
        raise ValueError("Debes ingresar una cadena válida.")

    return cadena[::-1]

def run():
    try:
        resultado = invertir_cadena("Hola mundo")
        print(resultado)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    run()