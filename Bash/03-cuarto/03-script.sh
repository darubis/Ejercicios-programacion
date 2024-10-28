#!/bin/bash

# Función para convertir grados Celsius a Fahrenheit y viceversa
convertir_grados() {
    local grados=$1
    local unidad=$2

    # Validación: Si no se ingresaron grados
    if [ -z "$grados" ]; then
        echo "No ingresaste grados a convertir"
        return
    fi

    # Validación: Si no se ingresó la unidad
    if [ -z "$unidad" ]; then
        echo "No ingresaste el tipo de unidad a convertir"
        return
    fi

    # Validación: Si unidad no es "C" o "F"
    if [[ "$unidad" != "C" && "$unidad" != "F" ]]; then
        echo "Valor de unidad no reconocido"
        return
    fi

    # Conversión
    if [ "$unidad" == "C" ]; then
        resultado=$(echo "scale=2; $grados * 9 / 5 + 32" | bc)
        echo "${grados}C = ${resultado}F"
    else
        resultado=$(echo "scale=2; ($grados - 32) * 5 / 9" | bc)
        echo "${grados}F = ${resultado}C"
    fi
}

# Ejemplos de prueba
convertir_grados               # No ingresaste grados a convertir
convertir_grados "2"           # No ingresaste el tipo de unidad a convertir
convertir_grados 2 "hola"      # Valor de unidad no reconocido
convertir_grados 2 "E"         # Valor de unidad no reconocido
convertir_grados 0 "C"         # 0C = 32F
convertir_grados 32 "F"        # 32F = 0C
convertir_grados 100 "F"       # 100F = 37.78C