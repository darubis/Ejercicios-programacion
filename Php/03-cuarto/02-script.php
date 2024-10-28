<?php

function numeroParImpar($numero = null) {
    // Validación para verificar si el número es null
    if (is_null($numero)) {
        echo "No ingresaste un número\n";
        return;
    }

    // Validación para verificar si el número es un entero
    if (!is_int($numero)) {
        echo "El valor '{$numero}' ingresado, No es un número\n";
        return;
    }

    // Verificar si el número es par o impar
    if ($numero % 2 === 0) {
        echo "El número {$numero} es Par\n";
    } else {
        echo "El número {$numero} es Impar\n";
    }
}

// Ejemplos de prueba
numeroParImpar();        // No ingresaste un número
numeroParImpar("54");    // El valor '54' ingresado, No es un número
numeroParImpar(-398);    // El número -398 es Par
numeroParImpar(19);      // El número 19 es Impar

?>