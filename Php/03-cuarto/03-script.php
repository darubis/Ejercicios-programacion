<?php

function convertirGrados($grados = null, $unidad = null) {
    // Validación: Si no se ingresaron grados
    if (is_null($grados)) {
        echo "No ingresaste grados a convertir\n";
        return;
    }

    // Validación: Si unidad es null
    if (is_null($unidad)) {
        echo "No ingresaste el tipo de unidad a convertir\n";
        return;
    }

    // Validación: Si unidad no es "C" o "F"
    if (strlen($unidad) != 1 || !in_array($unidad, ["C", "F"])) {
        echo "Valor de unidad no reconocido\n";
        return;
    }

    // Conversión
    if ($unidad === "C") {
        $resultado = round($grados * (9 / 5) + 32);
        echo "{$grados}C = {$resultado}F\n";
    } else {
        $resultado = round(($grados - 32) * (5 / 9));
        echo "{$grados}F = {$resultado}C\n";
    }
}

// Ejemplos de prueba
convertirGrados();               // No ingresaste grados a convertir
convertirGrados("2");             // No ingresaste el tipo de unidad a convertir
convertirGrados(2, "hola");       // Valor de unidad no reconocido
convertirGrados(2, "E");          // Valor de unidad no reconocido
convertirGrados(0, "C");          // 0C = 32F
convertirGrados(32, "F");         // 32F = 0C
convertirGrados(100, "F");        // 100F = 38C

?>