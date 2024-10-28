def es_primo(numero):
    # Si el número es menor o igual a 1, no es primo
    if numero <= 1:
        return False
    # El 2 y el 3 son primos
    if numero <= 3:
        return True
    # Si es divisible por 2 o 3, no es primo
    if numero % 2 == 0 or numero % 3 == 0:
        return False
    # Revisar divisores desde 5 hasta la raíz cuadrada del número
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True

def main():
    while True:
        try:
            # Pedir al usuario un número entero
            numero = int(input("Ingresa un número entero positivo: "))
            if numero < 0:
                raise ValueError("Debe ser un número positivo.")
            # Verificar si el número es primo
            if es_primo(numero):
                print(f"El número {numero} es primo.")
            else:
                print(f"El número {numero} no es primo.")
            break
        except ValueError as e:
            print(f"Entrada inválida: {e}. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()