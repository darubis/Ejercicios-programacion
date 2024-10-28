import java.util.Random;

public class Main {
    // Método para obtener un número aleatorio entre min y max
    public static int aleatorio1(int min, int max) {
        Random random = new Random();
        return random.nextInt((max - min + 1)) + min;
    }

    public static void main(String[] args) {
        // Llamada al método aleatorio1 para generar números entre 501 y 600
        for (int i = 0; i <= 10; i++) {
            System.out.println(aleatorio1(501, 600));
        }

        // Otra manera usando un lambda en Java
        Runnable aleatorio = () -> System.out.println(Math.round(Math.random() * 100 + 500));
        aleatorio.run();
    }
}
