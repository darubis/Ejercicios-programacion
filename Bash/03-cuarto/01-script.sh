#!/bin/bash

# Función para verificar si un número es primo
es_primo() {
    local num=$1
    if (( num <= 1 )); then
        return 1  # No es primo
    elif (( num <= 3 )); then
        return 0  # Es primo
    elif (( num % 2 == 0 || num % 3 == 0 )); then
        return 1  # No es primo si es divisible por 2 o 3
    fi

    local i=5
    while (( i * i <= num )); do
        if (( num % i == 0 || num % (i + 2) == 0 )); then
            return 1  # No es primo
        fi
        ((i += 6))
    done
    return 0  # Es primo
}

# Pedir al usuario que ingrese un número y validar la entrada
while true; do
    read -p "Ingresa un número entero positivo: " numero

    # Verificar si la entrada es un número entero positivo
    if [[ "$numero" =~ ^[0-9]+$ ]]; then
        # Verificar si el número es primo
        if es_primo "$numero"; then
            echo "El número $numero es primo."
        else
            echo "El número $numero no es primo."
        fi
        break
    else
        echo "Entrada inválida. Por favor, ingresa un número entero positivo."
    fi
done