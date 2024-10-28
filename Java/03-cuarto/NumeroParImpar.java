public class NumeroParImpar {

    public static void numeroParImpar(Object numero) {
        // Validación para verificar si el número es null
        if (numero == null) {
            System.out.println("No ingresaste un número");
            return;
        }

        // Validación para verificar si el número es de tipo Integer
        if (!(numero instanceof Integer)) {
            System.out.println("El valor " + numero + " ingresado, No es un número");
            return;
        }

        int num = (Integer) numero;
        // Verificar si es par o impar
        if (num % 2 == 0) {
            System.out.println("El número " + num + " es Par");
        } else {
            System.out.println("El número " + num + " es Impar");
        }
    }

    public static void main(String[] args) {
        numeroParImpar(null);        // No ingresaste un número
        numeroParImpar("54");        // El valor 54 ingresado, No es un número
        numeroParImpar(-398);        // El número -398 es Par
        numeroParImpar(19);          // El número 19 es Impar
    }
}