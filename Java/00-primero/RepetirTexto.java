public class RepetirTexto {

    public static void main(String[] args) {
        try {
            String resultado = repetirTexto("Hola mundo", 3);
            System.out.println(resultado);
        } catch (IllegalArgumentException e) {
            System.out.println(e.getMessage());
        }
    }

    public static String repetirTexto(String texto, int veces) {
        // Validaciones
        if (texto == null || veces <= 0) {
            throw new IllegalArgumentException("Debes ingresar un texto válido y una cantidad de veces mayor a 0.");
        }

        // Usando StringBuilder para construir la cadena repetida
        StringBuilder resultado = new StringBuilder();
        for (int i = 0; i < veces; i++) {
            resultado.append(texto);
            if (i < veces - 1) {
                resultado.append(" ");
            }
        }

        return resultado.toString();
    }
}