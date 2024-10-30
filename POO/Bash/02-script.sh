#!/bin/bash

# Clase CuentaBancaria simulada con funciones y variables globales
declare titular=""
declare saldo=0

# Función para inicializar la cuenta bancaria
function inicializar_cuenta() {
    titular=$1
    saldo=$2
}

# Función para depositar dinero
function depositar() {
    local cantidad=$1
    if (( $(echo "$cantidad > 0" | bc -l) )); then
        saldo=$(echo "$saldo + $cantidad" | bc)
    else
        echo "$cantidad no es una cantidad válida para depositar."
    fi
}

# Función para retirar dinero
function retirar() {
    local cantidad=$1
    if (( $(echo "$cantidad > 0 && $cantidad <= $saldo" | bc -l) )); then
        saldo=$(echo "$saldo - $cantidad" | bc)
    else
        echo "No se puede retirar esa cantidad; revise el saldo o la cantidad ingresada."
    fi
}

# Función para consultar el saldo actual
function consultar_saldo() {
    echo "Saldo actual: $saldo"
}

# Función para mostrar la información de la cuenta
function mostrar_informacion() {
    echo "La persona $titular cuenta con \$$saldo"
}

# Crear una instancia de cuenta bancaria y probar las funciones
inicializar_cuenta "Alberto" 500
mostrar_informacion

depositar 200
mostrar_informacion

retirar 800 # Prueba retirando una cantidad mayor al saldo
consultar_saldo # Muestra el saldo actual