#!/bin/bash

# Programa una funcion que cuente el numero de caracteres de una cadena de texto. 
# miFuncion("Hola mundo") devolvera 10

function contar_caracteres() {
    local cadena="$1"
    
    if [ -z "$cadena" ]; then
        echo "No ingresaste ninguna cadena"
    else
        echo "La cadena \"$cadena\" tiene ${#cadena} caracteres"
    fi
}

# Ejemplos de uso
contar_caracteres
contar_caracteres "Hola mundo"