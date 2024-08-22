public class EliminarCaracteres {

    public static void eliminarCaracteres(String texto, String patron) {
        if (texto == null || texto.isEmpty()) {
            System.out.println("No ingresaste un texto");
            return;
        }
        if (patron == null || patron.isEmpty()) {
            System.out.println("No ingresaste un patrón de caracteres");
            return;
        }

        String resultado = texto.replaceAll("(?i)" + patron, "");
        System.out.println(resultado);
    }

    public static void main(String[] args) {
        eliminarCaracteres("", ""); // No ingresaste un texto
        eliminarCaracteres("xyz1 xyz2 xyz3 xyz4 xyz5", ""); // No ingresaste un patrón de caracteres
        eliminarCaracteres("xyz1 xyz2 xyz3 xyz4 xyz5", "xyz"); // 1 2 3 4 5
    }
}