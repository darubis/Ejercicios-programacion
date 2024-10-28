/*
Programa una funcion que reciba un numero y evalue si es capicua o no (que se lee igual
en un sentido que en otro. ejemplo. miFuncion(2002) devolvera true) */

const capicua = (numero = 0) => {
    if (!numero) return console.warn("No ingresaste un numero");

    if (typeof numero !== "number") return console.warn(`El valor ${numero} ingresado. No es un numero`);

    numero = numero.toString();
    let alReves = numero.split("").reverse().join("");

    return (numero === alReves)
    ? console.info(`Si es capicua, numero original ${numero}, Numero al reves ${alReves}`)
    : console.info(`No es capicua, numero original ${numero}, numero alreves${alReves}`);
}

capicua();
capicua("2002");
capicua(2002);
capicua(212.212);