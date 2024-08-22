/**
    Programa si una funcion que valide si una palabra o frase es un palindromo (que se
    lee igual en un sentido que en otro). miFuncion("salas") devolvera true
 */


const palindromo = (palabra = "") => {
    if (!palabra) return console.warn("No ingresaste una palabra o frase");

    palabra = palabra.toLowerCase();
    let alReves  = palabra.split("").reverse().join("");

    return (palabra === alReves)
    ? console.info(`Si, es palindromo, palabra original ${palabra}. Palabra al reves ${alReves}`)
    : console.info(`No, es palindromo. Palabra original ${palabra}. Palabra al reves ${alReves}`)

}

palindromo();
palindromo("Hola mundo");
palindromo("Salas");