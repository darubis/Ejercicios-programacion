public class Main {
    // Método que evalúa si un número es capicúa
    public static void capicua(Object numero) {
        if (numero == null) {
            System.out.println("No ingresaste un número");
            return;
        }

        if (!(numero instanceof Number)) {
            System.out.println("El valor ingresado '" + numero + "' no es un número");
            return;
        }

        // Convertir el número a cadena
        String numeroStr = numero.toString();
        String alReves = new StringBuilder(numeroStr).reverse().toString();

        if (numeroStr.equals(alReves)) {
            System.out.println("Sí es capicúa, número original: " + numeroStr + ", número al revés: " + alReves);
        } else {
            System.out.println("No es capicúa, número original: " + numeroStr + ", número al revés: " + alReves);
        }
    }

    public static void main(String[] args) {
        // Pruebas de la función
        capicua(null);
        capicua("2002");
        capicua(2002);
        capicua(212.212);
    }
}