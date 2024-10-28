/*
Programa una funcion para convertir grados Celsius a Farenheit y viceversa, ejemplo
miFuncion(0, "C") devolvera 32F*/

const convertirGrados = (grados = undefined, unidad = undefined) => {
    if (grados === undefined) return console.warn("No ingresaste grados a convertir");
    
    if (typeof grados !== "number") return console.error(`El valor ${grados} ingresado,
        NO es un numero`);

    if (unidad === undefined) return console.warn("No ingresaste el tipo de dato a convertir");

    if (typeof unidad !== "string") return console.error(`El valor ${unidad} ingresado, No es una cadena de texto`);

    if (unidad.length !== 1 || !/(C|F)/.test(unidad)) return console.warn("Valor de unidad no reconocido");

    if(unidad === "C"){
        return console.info(`${grados}C = ${Math.round(grados * (9 / 5) + 32)}F`)
    }else{
        return console.info(`${grados}F = ${Math.round(((grados - 32) * (5 / 9)))}C`)
    }
}

convertirGrados();
convertirGrados("2");
convertirGrados(2);
convertirGrados(2,true);
convertirGrados(2,"hola");
convertirGrados(2,"E");
convertirGrados(0,"C");
convertirGrados(32,"F")
convertirGrados(100,"F")