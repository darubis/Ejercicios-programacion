/**
 * Programa que valida si una palabra o frase es un palíndromo (que se lee igual en un sentido que en otro).
 * miFuncion("salas") devolverá true
 */
public class Palindromo {

    public static void main(String[] args) {
        palindromo("");
        palindromo("Hola mundo");
        palindromo("Salas");
    }

    public static void palindromo(String palabra) {
        if (palabra == null || palabra.isEmpty()) {
            System.out.println("No ingresaste una palabra o frase");
            return;
        }

        palabra = palabra.toLowerCase();
        String alReves = new StringBuilder(palabra).reverse().toString();

        if (palabra.equals(alReves)) {
            System.out.println("Sí, es palíndromo. Palabra original: " + palabra + ". Palabra al revés: " + alReves);
        } else {
            System.out.println("No, no es palíndromo. Palabra original: " + palabra + ". Palabra al revés: " + alReves);
        }
    }
}