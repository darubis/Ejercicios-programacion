#!/usr/bin/env python3

# Ejercicio 3: Herencia
# Crea una clase base llamada Vehiculo con un atributo marca y un método mostrar_marca que imprima 
# la marca del vehículo.
# Crea una clase derivada llamada Auto que herede de Vehiculo y tenga un atributo adicional num_puertas.
# Crea un método en Auto llamado mostrar_detalles que imprima la marca y el número de puertas.
# Crea una instancia de Auto y muestra los detalles.

class Vehiculo:
    def __init__(self, marca: str):
        self.__marca = marca

    @property
    def marca(self) -> str:
        return self.__marca

    def mostrar_marca(self) -> None:
        print(f"La marca del vehículo es {self.__marca}")


class Auto(Vehiculo):
    def __init__(self, marca: str, num_puertas: int):
        super().__init__(marca)
        self.__num_puertas = num_puertas

    @property
    def num_puertas(self) -> int:
        return self.__num_puertas

    def mostrar_detalles(self) -> None:
        print(f"Este auto es un {self.marca} y tiene {self.num_puertas} puertas.")


# Crear una instancia de Auto y mostrar los detalles
auto1 = Auto("Toyota", 4)
auto1.mostrar_detalles()
auto1.mostrar_marca()  # También puedes mostrar la marca del vehículo
