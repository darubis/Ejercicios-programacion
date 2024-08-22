<?php
/**
 * Programa que valida si una palabra o frase es un palíndromo (que se lee igual en un sentido que en otro).
 * miFuncion("salas") devolverá true
 */

function palindromo($palabra = "") {
    if (empty($palabra)) {
        echo "No ingresaste una palabra o frase\n";
        return;
    }

    $palabra = strtolower($palabra);
    $alReves = strrev($palabra);

    if ($palabra === $alReves) {
        echo "Sí, es palíndromo. Palabra original: $palabra. Palabra al revés: $alReves\n";
    } else {
        echo "No, no es palíndromo. Palabra original: $palabra. Palabra al revés: $alReves\n";
    }
}

palindromo();
palindromo("Hola mundo");
palindromo("Salas");
?>