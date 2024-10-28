public class Main {
    // Método para calcular el factorial de un número
    public static void factorial(Integer numero) {
        if (numero == null) {
            System.out.println("No ingresaste un número");
            return;
        }

        if (!(numero instanceof Integer)) {
            System.out.println("El valor ingresado '" + numero + "' no es un número");
            return;
        }

        if (numero == 0) {
            System.out.println("El número no puede ser 0");
            return;
        }

        if (numero < 0) {
            System.out.println("El número no puede ser negativo");
            return;
        }

        int factorial = 1;
        for (int i = numero; i > 1; i--) {
            factorial *= i;
        }
        System.out.println("El factorial de " + numero + " es " + factorial);
    }

    public static void main(String[] args) {
        // Pruebas de la función
        factorial(null);
        factorial(0);
        factorial(-9);
        factorial(5);
        factorial(8);
    }
}