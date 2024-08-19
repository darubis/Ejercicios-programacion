#!/usr/bin/env python3

def repetir_texto(texto: str, veces: int) -> str:
    """Repite un texto una cantidad de veces.

    Args:
        texto (str): La cadena de texto a repetir.
        veces (int): El número de veces que se repetirá el texto.

    Returns:
        str: El texto repetido varias veces o un mensaje de error.
    """
    
    # Validaciones
    if not isinstance(texto, str) or not isinstance(veces, int):
        raise ValueError("Debes ingresar un texto (str) y una cantidad de veces (int) válidas.")
    
    if veces <= 0:
        raise ValueError("Debes ingresar una cantidad de veces válida (mayor que 0).")
    
    # Repetir el texto usando 'join'
    return " ".join([texto] * veces)

# Ejemplo de uso
try:
    texto_final = repetir_texto("Hola mundo", 3)
    print(texto_final)
except ValueError as e:
    print(e)