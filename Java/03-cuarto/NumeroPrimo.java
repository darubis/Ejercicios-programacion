public class NumeroPrimo {

    public static void numeroPrimo(Integer numero) {
        // Validaciones
        if (numero == null) {
            System.out.println("No ingresaste un número");
            return;
        }
        if (!(numero instanceof Integer)) {
            System.out.println("El valor ingresado no es un número");
            return;
        }
        if (numero == 0) {
            System.out.println("El número no puede ser 0");
            return;
        }
        if (numero == 1) {
            System.out.println("El número no puede ser 1");
            return;
        }
        if (numero < 0) {
            System.out.println("El número no puede ser negativo");
            return;
        }

        boolean divisible = false;

        for (int i = 2; i < numero; i++) {
            if (numero % i == 0) {
                divisible = true;
                break;
            }
        }

        if (!divisible) {
            System.out.println("El número " + numero + ", Sí es primo");
        } else {
            System.out.println("El número " + numero + ", No es primo");
        }
    }

    public static void main(String[] args) {
        numeroPrimo(5);   // El número 5, Sí es primo
        numeroPrimo(4);   // El número 4, No es primo
        numeroPrimo(null);
        numeroPrimo(null); // No ingresaste un número
        numeroPrimo(0);    // El número no puede ser 0
        numeroPrimo(1);    // El número no puede ser 1
        numeroPrimo(-1);   // El número no puede ser negativo
        numeroPrimo(13);   // El número 13, Sí es primo
        numeroPrimo(200);  // El número 200, No es primo
    }
}