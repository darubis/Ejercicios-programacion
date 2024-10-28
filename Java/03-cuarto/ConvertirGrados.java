public class ConvertirGrados {

    public static void convertirGrados(Double grados, String unidad) {
        // Validación: Si no se ingresaron grados
        if (grados == null) {
            System.out.println("No ingresaste grados a convertir");
            return;
        }

        // Validación: Si unidad es null
        if (unidad == null) {
            System.out.println("No ingresaste el tipo de unidad a convertir");
            return;
        }

        // Validación: Si unidad no es una cadena de texto "C" o "F"
        if (unidad.length() != 1 || (!unidad.equals("C") && !unidad.equals("F"))) {
            System.out.println("Valor de unidad no reconocido");
            return;
        }

        // Conversión
        if (unidad.equals("C")) {
            int resultado = (int) Math.round(grados * (9.0 / 5.0) + 32);
            System.out.println(grados + "C = " + resultado + "F");
        } else {
            int resultado = (int) Math.round((grados - 32) * (5.0 / 9.0));
            System.out.println(grados + "F = " + resultado + "C");
        }
    }

    public static void main(String[] args) {
        // Ejemplos de prueba
        convertirGrados(null, null);           // No ingresaste grados a convertir
        convertirGrados(Double.valueOf("2"), null); // No ingresaste el tipo de unidad a convertir
        convertirGrados(2.0, "hola");          // Valor de unidad no reconocido
        convertirGrados(2.0, "E");             // Valor de unidad no reconocido
        convertirGrados(0.0, "C");             // 0.0C = 32F
        convertirGrados(32.0, "F");            // 32.0F = 0C
        convertirGrados(100.0, "F");           // 100.0F = 38C
    }
}
