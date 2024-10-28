#!/bin/bash

# Definimos una función que representa una "clase" Persona
function Persona() {
    local nombre="$1"
    local edad="$2"
    echo "Hola, mi nombre es $nombre y tengo $edad años."
}

# Crear una instancia de Persona y mostrar el mensaje
Persona "Alberto" 45