class CuentaBancaria {
    constructor(titular, saldo) {
        this._titular = titular;
        this._saldo = saldo;
    }

    depositar(cantidad) {
        if (cantidad > 0) {
            this._saldo += cantidad;
        } else {
            console.log(`${cantidad} no es una cantidad válida para depositar.`);
        }
    }

    retirar(cantidad) {
        if (cantidad > 0 && cantidad <= this._saldo) {
            this._saldo -= cantidad;
        } else {
            console.log("No se puede retirar esa cantidad; revise el saldo o la cantidad ingresada.");
        }
    }

    consultarSaldo() {
        return this._saldo;
    }

    toString() {
        return `La persona ${this._titular} cuenta con $${this._saldo}`;
    }
}

// Crear una instancia y probar los métodos
const persona1 = new CuentaBancaria("Alberto", 500);
console.log(persona1.toString()); // Muestra el estado inicial

persona1.depositar(200);
console.log(persona1.toString()); // Muestra el estado después del depósito

persona1.retirar(800); // Intenta retirar una cantidad mayor al saldo para verificar el mensaje de error
console.log(persona1.consultarSaldo()); // Muestra el saldo actual