<?php
/**
 * Recorta el texto según el número de caracteres indicado.
 *
 * @param string $cadena La cadena de texto a recortar.
 * @param int $longitud El número de caracteres a mantener.
 * @return string La cadena recortada o un mensaje de error si los argumentos no son válidos.
 */

function recortar_texto($cadena, $longitud) {
    // Validar que la cadena no esté vacía y sea una cadena de texto
    if (!is_string($cadena) || empty($cadena)) {
        return "Debes ingresar una cadena válida.";
    }

    // Validar que longitud sea un número entero positivo
    if (!is_int($longitud) || $longitud < 0) {
        return "Debes ingresar una longitud válida.";
    }

    // Recortar el texto
    return substr($cadena, 0, $longitud);
}

// Ejemplo de uso
$cadena_recortada = recortar_texto("Hola mundo", 5);
echo $cadena_recortada . PHP_EOL;
?>