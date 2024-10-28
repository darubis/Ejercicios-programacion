<?php
// Función para calcular el factorial de un número
function factorial($numero = null) {
    if (is_null($numero)) {
        echo "No ingresaste un número\n";
        return;
    }

    if (!is_numeric($numero)) {
        echo "El valor ingresado '$numero' no es un número\n";
        return;
    }

    if ($numero == 0) {
        echo "El número no puede ser 0\n";
        return;
    }

    if ($numero < 0) {
        echo "El número no puede ser negativo\n";
        return;
    }

    $factorial = 1;
    for ($i = $numero; $i > 1; $i--) {
        $factorial *= $i;
    }

    echo "El factorial de $numero es $factorial\n";
}

// Pruebas de la función
factorial();
factorial("5");
factorial(0);
factorial(-9);
factorial(5);
factorial(8);
?>