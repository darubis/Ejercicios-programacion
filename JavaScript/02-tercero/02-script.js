/*
Programa una funcion que  calcule el factorial de un numero (El factorial de un
entero positivo n, se define como el producto de todos los numeros enteros desde 1
hasta n) ejemplo. miFuncion(5) devolvera 120 */

const factorial = (numero = undefined) => {
    if (numero === undefined) return console.warn("No ingresaste un numero");

    if (typeof numero !== "number") return console.warn(`El valor ${numero} ingresado. No es un numero`);

    if (numero === 0) return console.error("El numero no puede ser 0")

    if (Math.sign(numero) === -1)  return console.error("El numero no puede ser negativo")
    
    let factorial = 1;

    for (let i = numero; i > 1; i--){
        factorial *= i;
        // factorial = factorial * i;
    }
    return console.info(`El factorial de ${numero} es ${factorial}`);
}

factorial();
factorial("5");
factorial(0);
factorial(-9);
factorial(5);
factorial(8);