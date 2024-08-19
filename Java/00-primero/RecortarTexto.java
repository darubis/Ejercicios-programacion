public class RecortarTexto {

    /**
     * Recorta el texto según el número de caracteres indicado.
     * 
     * @param cadena La cadena de texto a recortar.
     * @param longitud El número de caracteres a mantener.
     * @return La cadena recortada o un mensaje de error si los argumentos no son válidos.
     */
    public static String recortarTexto(String cadena, int longitud) {
        // Validar que la cadena no esté vacía y sea una cadena de texto
        if (cadena == null || cadena.isEmpty()) {
            return "Debes ingresar una cadena válida.";
        }

        // Validar que longitud sea un número entero positivo
        if (longitud < 0) {
            return "Debes ingresar una longitud válida.";
        }

        // Recortar el texto
        return cadena.length() > longitud ? cadena.substring(0, longitud) : cadena;
    }

    public static void main(String[] args) {
        // Ejemplo de uso
        String cadenaRecortada = recortarTexto("Hola mundo", 5);
        System.out.println(cadenaRecortada);
    }
}