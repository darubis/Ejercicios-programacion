#!/usr/bin/env python3

# Ejercicio 6: Composición
# Crea una clase llamada Motor con un método encender que imprima "El motor está encendido".
# Crea una clase llamada Auto que tenga una instancia de Motor como atributo.
# Crea un método en Auto llamado encender_auto, que use el método encender de Motor.
# Prueba creando una instancia de Auto y encendiendo el motor a través del método encender_auto.


class Motor:
    def encender(self) -> None:
        print("El motor está encendido.")
        
    def apagar(self) -> None:
        print("El motor está apagado.")


class Auto:
    def __init__(self):
        self.__motor = Motor()

    def encender_auto(self) -> None:
        self.__motor.encender()

    def apagar_auto(self) -> None:
        self.__motor.apagar()


# Creando una instancia de Auto
mi_auto = Auto()

# Encendiendo el auto
mi_auto.encender_auto()

# Apagando el auto
mi_auto.apagar_auto()