/*
    Programa una funcion que invierta las palabras de una cadena de texto.
    miFuncion("Hola mundo") devolvera "odnum aloH"
 */

// const invertirCadena = (cadena = "") =>
// (!cadena)
// ? console.warn("No ingresaste una cadena de texto")
// : console.info(cadena.split("").reverse().join(""));

// invertirCadena();
// invertirCadena("Hola mundo");
// invertirCadena("JavaScript es un lenguaje de programacion increible");


//\/\/\/\/\/\/\/\/\\/\/\/\\/\\/\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\/\/\

const invertirCadena = (cadena = "") => {
    if (typeof cadena !== "string" || cadena.trim() === "") {
        console.warn("No ingresaste una cadena de texto válida");
        return;
    }
    const cadenaInvertida = cadena.split("").reverse().join("");
    console.info(cadenaInvertida);
};

invertirCadena();
invertirCadena("Hola mundo");
invertirCadena("JavaScript es un lenguaje de programación increíble");