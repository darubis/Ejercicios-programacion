/*Programa una funcion que repita un texto x veces, miFuncion("Hola mundo",3) devolvera
Hola mundo Hola mundo Hola mundo */


const repetirTexto = (cadena = "", veces = undefined) => {
    if (!cadena) {
        return console.warn("No ingresaste un texto");
    }
    
    if (veces === undefined) {
        return console.warn("No ingresaste el número de veces a repetir el texto");
    }

    if (veces === 0) {
        return console.error("El número de veces no puede ser 0");
    }

    if (Math.sign(veces) === -1) {
        return console.error("El número de veces no puede ser negativo");
    }

    // Construir la cadena repetida
    let resultado = "";
    for (let i = 0; i < veces; i++) {
        resultado += cadena + (i < veces - 1 ? " " : "");
    }

    // Imprimir el resultado
    console.log(resultado);
}

repetirTexto("Hola mundo", 3);