#!/usr/bin/env python3

# Ejercicio 10: Sobrecarga de Operadores

# Crea una clase Vector2D que represente un vector en dos dimensiones (x y y).
# Implementa el operador de suma __add__ para que puedas sumar dos objetos Vector2D y devolver un nuevo vector con la suma de sus componentes.
# Implementa el operador de multiplicación __mul__ para que puedas multiplicar un Vector2D por un escalar.
# Prueba creando dos vectores, sumándolos y multiplicando uno de ellos por un escalar.

class Vector2D:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __add__(self, other: 'Vector2D') -> 'Vector2D':
        if isinstance(other, Vector2D):
            return Vector2D(self.x + other.x, self.y + other.y)
        else:
            raise TypeError("Se esperaba un objeto Vector2D")

    def __mul__(self, scalar: float) -> 'Vector2D':
        if not isinstance(scalar, (int, float)):
            raise TypeError("Se esperaba un número para la multiplicación")
        return Vector2D(self.x * scalar, self.y * scalar)

    def __eq__(self, other: 'Vector2D') -> bool:
        return isinstance(other, Vector2D) and self.x == other.x and self.y == other.y

    def __str__(self) -> str:
        return f"Vector2D({self.x}, {self.y})"

# Creando vectores
v1 = Vector2D(2, 3)
v2 = Vector2D(1, -1)

# Sumando vectores
v3 = v1 + v2
print(v3)  # Imprime: Vector2D(3, 2)

# Multiplicando un vector por un escalar
v4 = v1 * 3
print(v4)  # Imprime: Vector2D(6, 9)

# Verificando igualdad entre vectores
v5 = Vector2D(3, 2)
print(v3 == v5)  # Imprime: True