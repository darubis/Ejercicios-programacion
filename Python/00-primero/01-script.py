#!/usr/bin/env python3

# Programa una funcion que te devuelva el texto recortado desgun el numero de caracteres
# indicado. miFuncion("Hola mundo",4) devolvera "Hola"


def recortar_texto(cadena: str, longitud: int) -> str:
    """Recorta el texto según el número de caracteres indicado.
    
    Args:
        cadena (str): La cadena de texto a recortar.
        longitud (int): El número de caracteres a mantener.
    
    Returns:
        str: La cadena recortada o un mensaje de error si los argumentos no son válidos.
    """
    if not isinstance(cadena, str) or not isinstance(longitud, int):
        return "Debes ingresar una cadena y una longitud válidas."
    
    if longitud < 0:
        return "La longitud debe ser un número entero positivo."

    return cadena[:longitud]

# Ejemplo de uso
cadena_recortada = recortar_texto("Hola mundo", 5)
print(cadena_recortada)

cadena_recortada = recortar_texto(87,5)
print(cadena_recortada)