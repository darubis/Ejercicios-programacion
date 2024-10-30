<?php

class Vehiculo {
    private $marca;

    public function __construct($marca) {
        $this->marca = $marca;
    }

    public function getMarca() {
        return $this->marca;
    }

    public function mostrarMarca() {
        echo "La marca del vehículo es {$this->marca}\n";
    }
}

class Auto extends Vehiculo {
    private $numPuertas;

    public function __construct($marca, $numPuertas) {
        parent::__construct($marca);
        $this->numPuertas = $numPuertas;
    }

    public function getNumPuertas() {
        return $this->numPuertas;
    }

    public function mostrarDetalles() {
        echo "Este auto es un {$this->getMarca()} y tiene {$this->numPuertas} puertas.\n";
    }
}

// Crear una instancia de Auto y mostrar los detalles
$auto1 = new Auto("Toyota", 4);
$auto1->mostrarDetalles();
$auto1->mostrarMarca(); // También puedes mostrar la marca del vehículo

?>