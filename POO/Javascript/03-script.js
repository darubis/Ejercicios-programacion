class Vehiculo {
    constructor(marca) {
        this._marca = marca;
    }

    get marca() {
        return this._marca;
    }

    mostrarMarca() {
        console.log(`La marca del vehículo es ${this._marca}`);
    }
}

class Auto extends Vehiculo {
    constructor(marca, numPuertas) {
        super(marca);
        this._numPuertas = numPuertas;
    }

    get numPuertas() {
        return this._numPuertas;
    }

    mostrarDetalles() {
        console.log(`Este auto es un ${this.marca} y tiene ${this.numPuertas} puertas.`);
    }
}

// Crear una instancia de Auto y mostrar los detalles
const auto1 = new Auto("Toyota", 4);
auto1.mostrarDetalles();
auto1.mostrarMarca();  // También puedes mostrar la marca del vehículo