<?php

function numeroPrimo($numero = null) {
    // Validaciones
    if (is_null($numero)) {
        echo "No ingresaste un número\n";
        return;
    }
    if (!is_int($numero)) {
        echo "El valor '{$numero}' ingresado no es un número\n";
        return;
    }
    if ($numero === 0) {
        echo "El número no puede ser 0\n";
        return;
    }
    if ($numero === 1) {
        echo "El número no puede ser 1\n";
        return;
    }
    if ($numero < 0) {
        echo "El número no puede ser negativo\n";
        return;
    }

    $divisible = false;

    for ($i = 2; $i < $numero; $i++) {
        if ($numero % $i === 0) {
            $divisible = true;
            break;
        }
    }

    if (!$divisible) {
        echo "El número {$numero}, Sí es primo\n";
    } else {
        echo "El número {$numero}, No es primo\n";
    }
}

// Ejemplos de prueba
numeroPrimo(5);   // El número 5, Sí es primo
numeroPrimo(4);   // El número 4, No es primo
numeroPrimo();    // No ingresaste un número
numeroPrimo("7"); // El valor '7' ingresado no es un número
numeroPrimo(true); // El valor '1' ingresado no es un número
numeroPrimo(0);    // El número no puede ser 0
numeroPrimo(1);    // El número no puede ser 1
numeroPrimo(-1);   // El número no puede ser negativo
numeroPrimo(13);   // El número 13, Sí es primo
numeroPrimo(200);  // El número 200, No es primo

?>