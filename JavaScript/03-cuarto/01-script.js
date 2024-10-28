/* Programa una función que determine si un número es primo (aquel que solo es divisible por sí mismo y 1) */

const primo = (numero = 0) => {
    // Validación de entrada
    if (!numero) return console.warn("No ingresaste un número");

    if (typeof numero !== "number") return console.warn(`El valor ${numero} ingresado no es un número`);

    if (numero <= 1) return console.warn("Debes ingresar un número mayor que 1");

    // Verificación de si es primo
    let esPrimo = true; // Asumimos que es primo

    for (let i = 2; i < numero; i++) {
        if (numero % i === 0) {
            esPrimo = false;
            break; // Salir del bucle si se encuentra un divisor
        }
    }

    // Resultado
    if (esPrimo) {
        console.log(`${numero} es un número primo`);
    } else {
        console.log(`${numero} no es un número primo`);
    }
};

primo(5); // 5 es un número primo
primo(4); // 4 no es un número primo


// ///////////////////////////////////////////////////////////////////////////////

// solucion jhon mircha

const numeroPrimo = (numero = undefined) => {

    // Validaciones
    if (numero == undefined) return console.warn("No ingresaste un número");
    if (typeof numero !== "number") return console.warn(`El valor ${numero} ingresado no es un número`);
    if (numero === 0) return console.error("El número no puede ser 0");
    if (numero === 1) return console.error("El número no puede ser 1");
    if (Math.sign(numero) === -1) return console.error("El número no puede ser negativo.");

    let divisible = false; // Inicialmente asumimos que no es divisible

    for (let i = 2; i < numero; i++) {
        if (numero % i === 0) {
            divisible = true; // Si encuentra un divisor, lo marcamos como no primo
            break; // Terminamos el bucle temprano
        }
    }

    return (!divisible)
        ? console.log(`El número ${numero}, Sí es primo`)
        : console.log(`El número ${numero}, No es primo`);
}

numeroPrimo(5); // El número 5, Sí es primo
numeroPrimo(4); // El número 4, No es primo


numeroPrimo();
numeroPrimo("7");
numeroPrimo(true);
numeroPrimo(0);
numeroPrimo(1);
numeroPrimo(-1);
numeroPrimo(13);
numeroPrimo(200);