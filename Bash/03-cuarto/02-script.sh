#!/bin/bash

# Programa una funcion que determine si un numero es par o impar. miFuncion(29)
# devolvera Impar

function es_par() {
    numero="$1"

    # Verificar que se haya ingresado un número
    if [ -z "$numero" ]; then
        echo "Debes ingresar un número"
        return
    fi

    # Verificar si el número es par o impar
    if (( numero % 2 == 0 )); then
        echo "El número $numero es par"
    else
        echo "El número $numero es impar"
    fi
}

# Llamadas a la función con diferentes valores
es_par 29    # Esperado: Impar
es_par -4    # Esperado: Par
es_par 12    # Esperado: Par
