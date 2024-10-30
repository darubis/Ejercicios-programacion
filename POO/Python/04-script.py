#!/usr/bin/env python3

# Ejercicio 4: Polimorfismo
# Crea una clase llamada Ave con un método volar que imprima "Esta ave vuela".
# Crea dos clases derivadas: Pato y Avestruz. En Pato, redefine el método volar para 
# que imprima "El pato vuela a baja altura", y en Avestruz, redefine el método para que 
# imprima "El avestruz no puede volar".
# Crea una función que reciba un objeto de tipo Ave y llame al método volar, para 
# demostrar el polimorfismo.

class Ave:
    def __init__(self, nombre: str):
        self.nombre = nombre

    def volar(self) -> None:
        print(f"{self.nombre} puede volar")


class Pato(Ave):
    def volar(self) -> None:
        print(f"{self.nombre}, el pato, vuela a baja altura")


class Avestruz(Ave):
    def volar(self) -> None:
        print(f"{self.nombre}, el avestruz, no puede volar")


# Función para demostrar el polimorfismo
def elegir_animal(tipo_ave: Ave) -> None:
    if isinstance(tipo_ave, Ave):
        tipo_ave.volar()
    else:
        print("El objeto no es un tipo de ave válido")


# Creación de instancias y prueba de polimorfismo
pato = Pato("Pato")
avestruz = Avestruz("Avestruz")

elegir_animal(pato)
elegir_animal(avestruz)