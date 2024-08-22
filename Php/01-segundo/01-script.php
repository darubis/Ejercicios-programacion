<?php

/**
 * Programa una función para contar el número de veces que se repite una palabra
 * en un texto largo. contarPalabra("Hola mundo adios mundo", "mundo") devolverá 2
 */

function contarPalabra($cadena = "", $palabra = "") {
    if (empty($cadena)) {
        echo "No ingresaste el texto largo" . PHP_EOL;
        return;
    }

    if (empty($palabra)) {
        echo "No ingresaste la palabra a evaluar" . PHP_EOL;
        return;
    }

    $contador = 0;
    $posicion = 0;

    while (($posicion = strpos($cadena, $palabra, $posicion)) !== false) {
        $contador++;
        $posicion++;
    }

    echo "La palabra '$palabra' se repite $contador veces" . PHP_EOL;
}

// Pruebas de la función
contarPalabra();
contarPalabra("", "mundo");
contarPalabra("hola mundo adios mundo");
contarPalabra("hola mundo adios mundo", "mundo");

?>