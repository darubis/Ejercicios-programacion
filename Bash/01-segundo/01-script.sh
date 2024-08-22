#!/bin/bash

# Función para contar el número de veces que se repite una palabra en un texto largo
function contar_palabra() {
    local texto="$1"
    local palabra="$2"

    if [[ -z "$texto" ]]; then
        echo "No ingresaste el texto largo"
        return
    fi

    if [[ -z "$palabra" ]]; then
        echo "No ingresaste la palabra a evaluar"
        return
    fi

    # Contar el número de coincidencias usando grep con expresiones regulares
    local contador=$(grep -o -w "$palabra" <<< "$texto" | wc -l)

    echo "La palabra '$palabra' se repite $contador veces"
}

# Pruebas de la función contar_palabra
contar_palabra ""
contar_palabra "Hola mundo adios mundo" ""
contar_palabra "Hola mundo adios mundo" "mundo"
contar_palabra "Este es un texto de prueba. Texto largo, texto corto y mas texto." "texto"