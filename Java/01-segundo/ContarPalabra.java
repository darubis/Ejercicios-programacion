public class ContarPalabra {

    /**
     * Programa una función para contar el número de veces que se repite una palabra
     * en un texto largo. contarPalabra("Hola mundo adios mundo", "mundo") devolverá 2
     */
    public static void contarPalabra(String cadena, String palabra) {
        if (cadena == null || cadena.isEmpty()) {
            System.out.println("No ingresaste el texto largo");
            return;
        }

        if (palabra == null || palabra.isEmpty()) {
            System.out.println("No ingresaste la palabra a evaluar");
            return;
        }

        int contador = 0;
        int i = 0;

        while ((i = cadena.indexOf(palabra, i)) != -1) {
            i += 1;
            contador++;
        }

        System.out.println("La palabra '" + palabra + "' se repite " + contador + " veces");
    }

    public static void main(String[] args) {
        // Pruebas de la función contarPalabra
        contarPalabra(null, "mundo");
        contarPalabra("", "mundo");
        contarPalabra("hola mundo adios mundo", null);
        contarPalabra("hola mundo adios mundo", "mundo");
    }
}