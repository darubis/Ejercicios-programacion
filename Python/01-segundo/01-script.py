def contar_palabra(cadena="", palabra=""):
    if not cadena:
        print("No ingresaste el texto largo")
        return

    if not palabra:
        print("No ingresaste la palabra a evaluar")
        return

    contador = 0
    i = 0

    while i != -1:
        i = cadena.find(palabra, i)
        if i != -1:
            i += 1
            contador += 1

    print(f"La palabra '{palabra}' se repite {contador} veces")

# Pruebas de la función
contar_palabra()
contar_palabra("", "mundo")
contar_palabra("hola mundo adios mundo")
contar_palabra("hola mundo adios mundo", "mundo")