<?php
/*
Programa una funcion que cuente el numero de caracteres de una cadena de texto. 
miFuncion("Hola mundo") devolvera 10 
*/

function contarCaracteres($cadena = "") {
    if (empty($cadena)) {
        echo "No ingresaste ninguna cadena\n";
    } else {
        echo "La cadena \"$cadena\" tiene " . strlen($cadena) . " caracteres\n";
    }
}

// Ejemplos de uso
contarCaracteres();           // Caso sin cadena
echo "\n";
contarCaracteres("Hola mundo"); // Caso con cadena
?>