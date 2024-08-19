<?php

/**
 * Convierte una cadena en un array de subcadenas separadas por el carácter dado.
 *
 * @param string $cadena La cadena de texto a dividir.
 * @param string $separador El carácter utilizado para dividir la cadena original.
 * @return array Un array de subcadenas.
 * @throws InvalidArgumentException Si la cadena es nula o vacía, o si el separador no es un solo carácter.
 */
function convertir_a_array(string $cadena, string $separador): array {
    // Validar que la cadena no esté vacía
    if (empty($cadena)) {
        throw new InvalidArgumentException("Debes ingresar una cadena válida.");
    }

    // Validar que el separador sea un solo carácter
    if (strlen($separador) !== 1) {
        throw new InvalidArgumentException("Debes ingresar un separador válido de un solo carácter.");
    }

    // Convertir la cadena en un array usando el separador
    return explode($separador, $cadena);
}

/**
 * Función principal que ejecuta el ejemplo de uso de la función convertir_a_array.
 */
function run() {
    try {
        // Ejemplo de uso
        $cadena = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Repellendus velit enim nulla non officia harum eum rerum ullam. Repellat accusamus doloribus odit ducimus nesciunt. Accusantium magni saepe excepturi possimus doloremque.";
        $separador = ' '; // Separador de un solo carácter
        
        $resultado = convertir_a_array($cadena, $separador);
        
        // Imprimir el resultado
        foreach ($resultado as $palabra) {
            echo $palabra . PHP_EOL;
        }
    } catch (InvalidArgumentException $e) {
        echo "Error: " . $e->getMessage() . PHP_EOL;
    }
}

// Ejecutar el script
run();