#!/bin/bash

# Variable para almacenar la marca y el número de puertas
marca=""
num_puertas=0

# Función para inicializar un vehículo
function inicializar_vehiculo() {
    marca=$1
}

# Función para mostrar la marca del vehículo
function mostrar_marca() {
    echo "La marca del vehículo es $marca"
}

# Función para inicializar un auto con marca y número de puertas
function inicializar_auto() {
    inicializar_vehiculo "$1"
    num_puertas=$2
}

# Función para mostrar los detalles del auto
function mostrar_detalles() {
    echo "Este auto es un $marca y tiene $num_puertas puertas."
}

# Crear una instancia de Auto y mostrar los detalles
inicializar_auto "Toyota" 4
mostrar_detalles
mostrar_marca