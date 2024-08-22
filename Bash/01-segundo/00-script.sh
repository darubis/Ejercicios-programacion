#!/bin/bash

# Función que invierte las palabras de una cadena de texto
invertir_cadena() {
    local cadena="$1"
    
    if [[ -z "$cadena" ]]; then
        echo "Debes ingresar una cadena válida." >&2
        return 1
    fi

    echo "$cadena" | rev
}

# Función principal para ejecutar el script
function run() {
    local resultado
    resultado=$(invertir_cadena "Hola mundo")
    
    if [[ $? -eq 0 ]]; then
        echo "$resultado"
    else
        echo "Error: No se pudo invertir la cadena." >&2
    fi
}

# Ejecutar la función principal
run