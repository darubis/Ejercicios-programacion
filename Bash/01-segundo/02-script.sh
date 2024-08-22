#!/bin/bash

# Programa que valida si una palabra o frase es un palíndromo (que se lee igual en un sentido que en otro).
# miFuncion("salas") devolverá true

function palindromo() {
    local palabra="$1"
    palabra=$(echo "$palabra" | tr -d ' ' | tr '[:upper:]' '[:lower:]')
    palabra_invertida=$(echo "$palabra" | rev)

    if [[ "$palabra" == "$palabra_invertida" ]]; then
        return 0
    else
        return 1
    fi
}

function run() {
    read -p "Ingresa una palabra: " palabra

    if palindromo "$palabra"; then
        echo "Es palíndromo"
    else
        echo "No es palíndromo"
    fi
}

run