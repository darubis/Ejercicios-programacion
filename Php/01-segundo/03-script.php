<?php
/**
 * Programa que elimina cierto patrón de caracteres de un texto dado.
 * miFuncion("xyz1 xyz2 xyz3 xyz4 xyz5") devolverá "1 2 3 4 5"
 */

function eliminarCaracteres($texto = "", $patron = "") {
    if (empty($texto)) {
        echo "No ingresaste un texto\n";
        return;
    }
    if (empty($patron)) {
        echo "No ingresaste un patrón de caracteres\n";
        return;
    }

    $resultado = preg_replace("/$patron/i", "", $texto);
    echo $resultado . "\n";
}

// Ejemplos de uso
eliminarCaracteres();
eliminarCaracteres("xyz1 xyz2 xyz3 xyz4 xyz5");
eliminarCaracteres("xyz1 xyz2 xyz3 xyz4 xyz5", "xyz");
?>