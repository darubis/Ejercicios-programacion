public class Persona {
    private String nombre;
    private int edad;

    public Persona(String nombre, int edad) {
        this.nombre = nombre;
        this.edad = edad;
    }

    @Override
    public String toString() {
        return "Hola, mi nombre es " + nombre + " y tengo " + edad + " años.";
    }

    public static void main(String[] args) {
        Persona persona1 = new Persona("Alberto", 45);
        System.out.println(persona1);
    }
}