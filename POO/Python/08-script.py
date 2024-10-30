#!/usr/bin/env python3

# Ejercicio 8: Interfaces (Abstract Base Class)

# Crea una clase abstracta llamada Forma que tenga un método abstracto area.
# Crea dos clases Rectangulo y Circulo que hereden de Forma e implementen el método area.
#        En Rectangulo, calcula el área usando base * altura.
#       En Circulo, calcula el área usando pi * radio^2 (usa math.pi).
# Crea una función que reciba una lista de formas y devuelva el área total.
# Prueba creando varias instancias de Rectangulo y Circulo, y usando la función para calcular el área total.

import abc
import math
from typing import List

# Clase abstracta Forma
class Forma(abc.ABC):
    @abc.abstractmethod
    def area(self) -> float:
        """Calcula el área de la forma."""
        pass

# Clase Rectángulo
class Rectangulo(Forma):
    def __init__(self, base: float, altura: float):
        if base <= 0 or altura <= 0:
            raise ValueError("La base y la altura deben ser mayores que cero.")
        self.base = base
        self.altura = altura

    @property
    def area(self) -> float:
        return self.base * self.altura

# Clase Círculo
class Circulo(Forma):
    def __init__(self, radio: float):
        if radio <= 0:
            raise ValueError("El radio debe ser mayor que cero.")
        self.radio = radio

    @property
    def area(self) -> float:
        return math.pi * self.radio**2

# Función para calcular el área total de una lista de formas
def area_total(formas: List[Forma]) -> float:
    return sum(forma.area for forma in formas)

# Creando instancias de Rectángulo y Círculo
rectangulo1 = Rectangulo(5, 3)
rectangulo2 = Rectangulo(10, 2)
circulo1 = Circulo(4)
circulo2 = Circulo(2)

# Lista de formas
formas = [rectangulo1, rectangulo2, circulo1, circulo2]

# Calculando el área total
area_total_valor = area_total(formas)
print("El área total es:", area_total_valor)