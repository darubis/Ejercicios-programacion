public class InvertirCadena {

    /**
     * Programa una función que invierte las palabras de una cadena de texto.
     * miFuncion("Hola mundo") devolverá "odnum aloH"
     */
    public static String invertirCadena(String cadena) {
        if (cadena == null || cadena.trim().isEmpty()) {
            return "No ingresaste una cadena de texto válida";
        }
        return new StringBuilder(cadena).reverse().toString();
    }

    public static void main(String[] args) {
        // Pruebas de la función invertirCadena
        System.out.println(invertirCadena(null));
        System.out.println(invertirCadena("Hola mundo"));
        System.out.println(invertirCadena("Java es un lenguaje de programación increíble"));
    }
}