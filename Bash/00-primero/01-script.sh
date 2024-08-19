#!/bin/bash

# Programa una funcion que te devuelva el texto recortado desgun el numero de caracteres
# indicado. miFuncion("Hola mundo",4) devolvera "Hola"


function recortar_texto() {
    local cadena="$1"
    local longitud="$2"
    
    # Validar que la cadena no esté vacía
    if [ -z "$cadena" ]; then
        echo "Debes ingresar una cadena válida"
        return
    fi
    
    # Validar que longitud sea un número entero positivo
    if ! [[ "$longitud" =~ ^[0-9]+$ ]] || [ "$longitud" -lt 0 ]; then
        echo "Debes ingresar una longitud válida"
        return
    fi

    # Recortar el texto
    echo "${cadena:0:$longitud}"
}

# Ejemplo de uso
cadena_recortada=$(recortar_texto "Hola mundo" 5)
echo "$cadena_recortada"