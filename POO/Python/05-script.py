#!/usr/bin/env python3


# Ejercicio 5: Métodos y Atributos de Clase

# Crea una clase llamada ContadorObjetos que tenga un atributo de clase llamado cantidad_objetos, 
# inicializado en 0.
# Cada vez que se cree una nueva instancia de ContadorObjetos, incrementa cantidad_objetos en 1.
# Crea un método de clase mostrar_cantidad que imprima la cantidad de objetos creados.
# Prueba creando varias instancias de ContadorObjetos y llamando a mostrar_cantidad.

class ContadorObjetos:
    cantidad_objetos: int = 0

    def __init__(self):
        ContadorObjetos.cantidad_objetos += 1

    @classmethod
    def mostrar_cantidad(cls) -> None:
        print(f"Se han creado {cls.cantidad_objetos} objetos.")

    def __str__(self) -> str:
        return f"Instancia del objeto número {ContadorObjetos.cantidad_objetos}"

# Creando varias instancias
objeto1 = ContadorObjetos()
objeto2 = ContadorObjetos()
objeto3 = ContadorObjetos()

# Mostrando la cantidad de objetos
ContadorObjetos.mostrar_cantidad()

# Ejemplo opcional de uso de __str__
print(objeto1)