#!/usr/bin/env python3

# Ejercicio 7: Método estático

#  Crea una clase llamada Calculadora.
# Agrega un método estático llamado suma que reciba dos números y devuelva su suma.
# Agrega otro método estático llamado resta que reciba dos números y devuelva su diferencia.
# Prueba llamando a Calculadora.suma y Calculadora.resta sin necesidad de crear una instancia de la clase.

class Calculadora:
    @staticmethod
    def suma(a: float, b: float) -> float:
        """Suma dos números.

        Args:
            a (float): Primer número.
            b (float): Segundo número.

        Returns:
            float: La suma de a y b.
        """
        return a + b

    @staticmethod
    def resta(a: float, b: float) -> float:
        """Resta dos números.

        Args:
            a (float): Minuendo.
            b (float): Sustraendo.

        Returns:
            float: La diferencia entre a y b.
        """
        return a - b

    @staticmethod
    def multiplicacion(a: float, b: float) -> float:
        """Multiplica dos números.

        Args:
            a (float): Primer número.
            b (float): Segundo número.

        Returns:
            float: El producto de a y b.
        """
        return a * b

    @staticmethod
    def division(a: float, b: float) -> float:
        """Divide dos números, manejando la división entre cero.

        Args:
            a (float): Dividendo.
            b (float): Divisor.

        Returns:
            float: El cociente de a y b, o 'None' si b es cero.
        """
        return a / b if b != 0 else None

# Usando los métodos estáticos sin crear una instancia
resultado_suma = Calculadora.suma(5, 3)
print(resultado_suma)  # Imprime: 8

resultado_resta = Calculadora.resta(10, 4)
print(resultado_resta)  # Imprime: 6

resultado_multiplicacion = Calculadora.multiplicacion(3, 4)
print(resultado_multiplicacion)  # Imprime: 12

resultado_division = Calculadora.division(12, 4)
print(resultado_division)  # Imprime: 3.0