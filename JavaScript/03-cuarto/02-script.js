/*
Programa una funcion que determine si un numero es par o impar. miFuncion(29)
devolvera Impar */

const es_par = (numero) => {
    if (!numero) return console.warn("Debes ingresar un numero");

    return (numero % 2)
        ? console.log(`El número ${numero}, es impar`)
        : console.log(`El número ${numero}, Sí es par`);
}

// es_par();
// es_par(29);
// es_par(4);
// es_par(7);


//////////////////////////////////////////////////////////////////

// solucion jhon mircha

const numeroParImpar = (numero = undefined) => {
    if (numero === undefined) return console.warn("No ingresaste un numero");

    if (typeof numero != "number") return console.error(`El valor ${numero} ingresado, No es un numero`);

    return ((numero % 2) === 0)
        ? console.info(`El numero ${numero} es Par`)
        : console.info(`El numero ${numero} es Impar`);
}

numeroParImpar();
numeroParImpar("54");
numeroParImpar(-398);
numeroParImpar(19);