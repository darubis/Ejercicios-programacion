<?php

/**
 * Programa una función que invierte las palabras de una cadena de texto.
 * miFuncion("Hola mundo") devolverá "odnum aloH"
 */

function invertirCadena($cadena = "") {
    if (!is_string($cadena) || trim($cadena) === "") {
        return "No ingresaste una cadena de texto válida";
    }
    return strrev($cadena);
}

// Pruebas de la función invertirCadena
echo invertirCadena() . PHP_EOL;
echo invertirCadena("Hola mundo") . PHP_EOL;
echo invertirCadena("PHP es un lenguaje de programacion increible") . PHP_EOL;

?>