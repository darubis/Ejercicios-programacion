#!/bin/bash

# Programa que elimina cierto patrón de caracteres de un texto dado.
# miFuncion("xyz1 xyz2 xyz3 xyz4 xyz5") devolverá "1 2 3 4 5"

function eliminar_caracteres() {
    local texto="$1"
    local patron="$2"

    if [[ -z "$texto" ]]; then
        echo "No ingresaste un texto"
        return
    fi

    if [[ -z "$patron" ]]; then
        echo "No ingresaste un patrón de caracteres"
        return
    fi

    # Eliminar el patrón del texto utilizando sed
    local resultado=$(echo "$texto" | sed "s/$patron//gI")
    echo "$resultado"
}

# Ejemplos de uso
eliminar_caracteres
eliminar_caracteres "xyz1 xyz2 xyz3 xyz4 xyz5"
eliminar_caracteres "xyz1 xyz2 xyz3 xyz4 xyz5" "xyz"