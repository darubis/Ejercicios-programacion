#!/bin/bash

# Función para repetir un texto una cantidad de veces
repetir_texto() {
    local texto="$1"
    local veces="$2"

    # Validaciones
    if ! [[ "$veces" =~ ^[0-9]+$ ]] || [ "$veces" -le 0 ]; then
        echo "Debes ingresar una cantidad de veces válida (entero positivo)."
        return 1
    fi

    # Repetir el texto
    for ((i=0; i<veces; i++)); do
        echo -n "$texto "
    done
    echo
}

# Ejemplo de uso
repetir_texto "Hola mundo" 3