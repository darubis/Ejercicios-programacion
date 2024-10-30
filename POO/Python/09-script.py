#!/usr/bin/env python3

# Ejercicio 9: Herencia Múltiple y MRO (Method Resolution Order)

# Crea una clase llamada SerVivo con un método respirar que imprima "Este ser vivo está respirando".
# Crea una clase Mamifero que herede de SerVivo y tenga un método mamar que imprima "Este mamífero está mamando".
# Crea una clase Humano que herede tanto de SerVivo como de Mamifero y tenga un método hablar que imprima "Este humano está hablando".
# Crea una instancia de Humano y llama a los métodos respirar, mamar y hablar.
# Usa __mro__ para mostrar el orden de resolución de métodos de la clase Humano.

class SerVivo:
    def respirar(self) -> None:
        print("Este ser vivo está respirando")


class Mamifero:
    def mamar(self) -> None:
        print("Este mamífero está mamando")


class Humano(SerVivo, Mamifero):
    def hablar(self) -> None:
        print("Este humano está hablando")


# Creando una instancia de Humano
humano1 = Humano()

# Llamando a los métodos
humano1.respirar()
humano1.mamar()
humano1.hablar()

# Mostrando el MRO
print("\nOrden de resolución de métodos (MRO):")
for cls in Humano.__mro__:
    print(cls)