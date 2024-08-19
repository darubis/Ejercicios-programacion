<?php

function repetirTexto($texto, $veces) {
    // Validaciones
    if (!is_string($texto) || !is_int($veces) || $veces <= 0) {
        return "Debes ingresar un texto válido y una cantidad de veces mayor a 0.";
    }

    // Repetir el texto
    $resultado = str_repeat($texto . ' ', $veces);
    
    // Eliminar el último espacio extra al final de la cadena
    return trim($resultado);
}

// Ejemplo de uso
echo repetirTexto("Hola mundo", 3);

?>