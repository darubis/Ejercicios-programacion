# Ejercicio 1: Clases y Objetos

# Crea una clase llamada Persona con las propiedades nombre y edad.
# Crea un método llamado saludar que imprima un mensaje de saludo, como "Hola, mi nombre es <nombre> y tengo <edad> años."
# Crea una instancia de la clase Persona con tu nombre y edad y llama al método saludar.


class Persona:
    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad

    def __str__(self) -> str:
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años."

persona1 = Persona("Alberto", 45)
print(persona1)