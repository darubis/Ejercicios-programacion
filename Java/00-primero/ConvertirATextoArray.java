public class ConvertirATextoArray {

    /**
     * Convierte una cadena en un array de subcadenas separadas por el carácter dado.
     *
     * @param cadena La cadena de texto a dividir.
     * @param separador El carácter utilizado para dividir la cadena original.
     * @return Un array de subcadenas.
     * @throws IllegalArgumentException Si la cadena es nula o vacía, o si el separador no es un solo carácter.
     */
    public static String[] convertirATextoArray(String cadena, char separador) {
        // Validar que la cadena no esté vacía
        if (cadena == null || cadena.isEmpty()) {
            throw new IllegalArgumentException("Debes ingresar una cadena válida.");
        }

        // Validar que el separador sea un solo carácter
        if (Character.toString(separador).length() != 1) {
            throw new IllegalArgumentException("Debes ingresar un separador válido de un solo carácter.");
        }

        // Convertir la cadena en un array usando el separador
        return cadena.split(Character.toString(separador));
    }

    public static void main(String[] args) {
        try {
            // Ejemplo de uso
            String cadena = "Lorem ipsum dolor sit amet consectetur adipisicing elit";
            char separador = ' '; // Separador de un solo carácter
            
            String[] resultado = convertirATextoArray(cadena, separador);
            
            // Imprimir el resultado
            for (String palabra : resultado) {
                System.out.println(palabra);
            }
        } catch (IllegalArgumentException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}