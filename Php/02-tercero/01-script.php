<?php
// Función para obtener un número aleatorio entre min y max
function aleatorio1($min, $max) {
    return rand($min, $max);
}

// Llamada a la función aleatorio1 para generar números entre 501 y 600
for ($i = 0; $i <= 10; $i++) {
    echo aleatorio1(501, 600) . "\n";
}

// Otra manera de generar un número aleatorio entre 501 y 600
$aleatorio = function() {
    echo round(mt_rand(0, 100) + 500) . "\n";
};
$aleatorio();
?>