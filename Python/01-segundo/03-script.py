#!/usr/bin/env python3

# Porgrama una funcion que elimine cierto patron de caracteres de un texto dado.
# miFuncion("xyz1 xyz2 xyz3 xyz4 xyz5") devolvera "1,2,3,4 y 5"

import re

def eliminar_caracteres(texto="", patron=""):
    if not texto:
        print("No ingresaste un texto")
        return
    if not patron:
        print("No ingresaste un patrón de caracteres")
        return

    resultado = re.sub(patron, "", texto, flags=re.IGNORECASE)
    print(resultado)

# Ejemplos de uso
eliminar_caracteres()
eliminar_caracteres("xyz1 xyz2 xyz3 xyz4 xyz5")
eliminar_caracteres("xyz1 xyz2 xyz3 xyz4 xyz5", "xyz")