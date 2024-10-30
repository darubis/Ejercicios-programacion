<?php

class CuentaBancaria {
    private $titular;
    private $saldo;

    public function __construct($titular, $saldo) {
        $this->titular = $titular;
        $this->saldo = $saldo;
    }

    public function depositar($cantidad) {
        if ($cantidad > 0) {
            $this->saldo += $cantidad;
        } else {
            echo "$cantidad no es una cantidad válida para depositar.\n";
        }
    }

    public function retirar($cantidad) {
        if ($cantidad > 0 && $cantidad <= $this->saldo) {
            $this->saldo -= $cantidad;
        } else {
            echo "No se puede retirar esa cantidad; revise el saldo o la cantidad ingresada.\n";
        }
    }

    public function consultarSaldo() {
        return $this->saldo;
    }

    public function __toString() {
        return "La persona {$this->titular} cuenta con \${$this->saldo}\n";
    }
}

// Crear una instancia y probar los métodos
$persona1 = new CuentaBancaria("Alberto", 500);
echo $persona1; // Muestra el estado inicial

$persona1->depositar(200);
echo $persona1; // Muestra el estado después del depósito

$persona1->retirar(800); // Intenta retirar una cantidad mayor al saldo para verificar el mensaje de error
echo "Saldo actual: " . $persona1->consultarSaldo() . "\n"; // Muestra el saldo actual
?>