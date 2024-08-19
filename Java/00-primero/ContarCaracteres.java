/*
 Programa una funcion que cuente el numero de caracteres de una cadena de texto. 
miFuncion("Hola mundo") devolvera 10 
 */

public class ContarCaracteres {

    public static void contarCaracteres(String cadena) {
        if (cadena == null || cadena.isEmpty()) {
            System.out.println("No ingresaste ninguna cadena");
        } else {
            System.out.println("La cadena \"" + cadena + "\" tiene " + cadena.length() + " caracteres");
        }
    }

    public static void main(String[] args) {
        contarCaracteres("");            // Caso sin cadena
        contarCaracteres("Hola mundo");  // Caso con cadena
    }
}