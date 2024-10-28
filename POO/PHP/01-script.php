<?php

class Persona {
    private $nombre;
    private $edad;

    public function __construct($nombre, $edad) {
        $this->nombre = $nombre;
        $this->edad = $edad;
    }

    public function __toString() {
        return "Hola, mi nombre es {$this->nombre} y tengo {$this->edad} años.";
    }
}

$persona1 = new Persona("Alberto", 45);
echo $persona1;