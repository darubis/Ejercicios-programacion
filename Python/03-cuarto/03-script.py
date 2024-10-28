def convertir_grados(grados=None, unidad=None):
    # Validación: Si no se ingresaron grados
    if grados is None:
        print("No ingresaste grados a convertir")
        return

    # Validación: Si grados no es un número
    if not isinstance(grados, (int, float)):
        print(f"El valor '{grados}' ingresado, NO es un número")
        return

    # Validación: Si no se ingresó la unidad
    if unidad is None:
        print("No ingresaste el tipo de unidad a convertir")
        return

    # Validación: Si unidad no es una cadena
    if not isinstance(unidad, str):
        print(f"El valor '{unidad}' ingresado, NO es una cadena de texto")
        return

    # Validación: Si unidad no es 'C' o 'F'
    if len(unidad) != 1 or unidad not in ('C', 'F'):
        print("Valor de unidad no reconocido")
        return

    # Conversión
    if unidad == "C":
        resultado = round(grados * (9 / 5) + 32)
        print(f"{grados}C = {resultado}F")
    else:
        resultado = round((grados - 32) * (5 / 9))
        print(f"{grados}F = {resultado}C")

# Ejemplos de prueba
convertir_grados()             # No ingresaste grados a convertir
convertir_grados("2")          # El valor '2' ingresado, NO es un número
convertir_grados(2)            # No ingresaste el tipo de unidad a convertir
convertir_grados(2, True)      # El valor 'True' ingresado, NO es una cadena de texto
convertir_grados(2, "hola")    # Valor de unidad no reconocido
convertir_grados(2, "E")       # Valor de unidad no reconocido
convertir_grados(0, "C")       # 0C = 32F
convertir_grados(32, "F")      # 32F = 0C
convertir_grados(100, "F")