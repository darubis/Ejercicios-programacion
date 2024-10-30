class Vehiculo {
    private String marca;

    public Vehiculo(String marca) {
        this.marca = marca;
    }

    public String getMarca() {
        return marca;
    }

    public void mostrarMarca() {
        System.out.println("La marca del vehículo es " + marca);
    }
}

class Auto extends Vehiculo {
    private int numPuertas;

    public Auto(String marca, int numPuertas) {
        super(marca);
        this.numPuertas = numPuertas;
    }

    public int getNumPuertas() {
        return numPuertas;
    }

    public void mostrarDetalles() {
        System.out.println("Este auto es un " + getMarca() + " y tiene " + numPuertas + " puertas.");
    }
}

public class Main {
    public static void main(String[] args) {
        Auto auto1 = new Auto("Toyota", 4);
        auto1.mostrarDetalles();
        auto1.mostrarMarca(); // También puedes mostrar la marca del vehículo
    }
}