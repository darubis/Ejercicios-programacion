<?php
// Función que evalúa si un número es capicúa
function capicua($numero = 0) {
    if ($numero === 0) {
        echo "No ingresaste un número\n";
        return;
    }

    if (!is_numeric($numero)) {
        echo "El valor ingresado '$numero' no es un número\n";
        return;
    }

    $numero = strval($numero);
    $alReves = strrev($numero);

    if ($numero === $alReves) {
        echo "Sí es capicúa, número original: $numero, número al revés: $alReves\n";
    } else {
        echo "No es capicúa, número original: $numero, número al revés: $alReves\n";
    }
}

// Pruebas de la función
capicua();
capicua("2002");
capicua(2002);
capicua(212.212);
?>