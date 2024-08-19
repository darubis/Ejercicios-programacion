#!/usr/bin/env python3

def convertir_a_array(cadena: str, separador: str) -> list:
    """
    Convierte una cadena en una lista de subcadenas separadas por el carácter dado.

    Args:
        cadena (str): La cadena de texto a dividir.
        separador (str): El carácter o cadena utilizada para dividir la cadena original.

    Returns:
        list: Una lista de subcadenas.

    Raises:
        ValueError: Si la cadena no es válida o el separador no es un solo carácter.
    """
    if not isinstance(cadena, str) or not cadena:
        raise ValueError("Debes ingresar una cadena válida.")

    if not isinstance(separador, str) or len(separador) != 1:
        raise ValueError("Debes ingresar un separador válido de un solo carácter.")

    return cadena.split(separador)


def run():
    """
    Función principal que ejecuta el ejemplo de uso de la función convertir_a_array.
    """
    try:
        resultado = convertir_a_array(
            "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Repellendus velit enim nulla non officia harum eum rerum ullam. Repellat accusamus doloribus odit ducimus nesciunt. Accusantium magni saepe excepturi possimus doloremque.", " ")
        print(resultado)
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    run()