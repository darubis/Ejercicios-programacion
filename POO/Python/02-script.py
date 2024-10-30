#!/usr/bin/env python3

# Ejercicio 2: Encapsulamiento
# Crea una clase llamada CuentaBancaria con los atributos privados titular y saldo.
# Crea métodos públicos depositar(cantidad) y retirar(cantidad) que modifiquen el saldo.
# Si el retiro excede el saldo, muestra un mensaje que indique que no es posible 
# realizar la operación.
# Crea un método que permita consultar el saldo.

class CuentaBancaria:
    def __init__(self, titular: str, saldo: float):
        self.__titular = titular
        self.__saldo = saldo

    def depositar(self, cantidad: float):
        if cantidad > 0:
            self.__saldo += cantidad
        else:
            print(f"{cantidad} no es una cantidad válida para depositar.")

    def retirar(self, cantidad: float):
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
        else:
            print("No se puede retirar esa cantidad; revise el saldo o la cantidad ingresada.")

    def consultar_saldo(self) -> float:
        return self.__saldo

    def __str__(self) -> str:
        return f"La persona {self.__titular} cuenta con ${self.__saldo}"

persona1 = CuentaBancaria("Alberto", 500)
print(persona1)

persona1.depositar(200)
print(persona1)

persona1.retirar(800)  # Prueba retirando una cantidad mayor al saldo para verificar el mensaje de error
print(persona1.consultar_saldo())  # Muestra el saldo actual