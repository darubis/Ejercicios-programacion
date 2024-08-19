#!/bin/bash

# Programa una funcion que dada una String te devuelva un Array de textos separados por 
# cierto caracter. miFuncion("Hola que tal","") devolvera ["Hola", "que", "tal"] 



function convertir_a_array() {
    local cadena="$1"
    local separador="$2"
    
    # Validar que la cadena no esté vacía
    if [ -z "$cadena" ]; then
        echo "Debes ingresar una cadena válida."
        return 1
    fi
    
    # Validar que el separador sea un solo carácter
    if [ ${#separador} -ne 1 ]; then
        echo "Debes ingresar un separador válido de un solo carácter."
        return 1
    fi
    
    # Convertir la cadena en un array usando el separador
    IFS="$separador" read -ra array <<< "$cadena"
    
    # Imprimir el array
    echo "${array[@]}"
}

# Función principal que ejecuta el ejemplo de uso
function run() {
    local cadena="Lorem ipsum dolor sit amet, consectetur adipisicing elit. Repellendus velit enim nulla non officia harum eum rerum ullam. Repellat accusamus doloribus odit ducimus nesciunt. Accusantium magni saepe excepturi possimus doloremque."
    local separador=" "
    
    resultado=$(convertir_a_array "$cadena" "$separador")
    
    if [ $? -eq 0 ]; then
        echo "$resultado"
    fi
}

# Ejecutar el script
run
