/*Programa una funcion que te devuelva el texto recortado desgun el numero de caracteres
indicado. miFuncion("Hola mundo",4) devolvera "Hola" */

const recortarTexto = (cadena = "", longitud = undefined) => 
(!cadena)
? console.warn("No ingresaste una cadena de texto")
: (longitud == undefined)
? console.warn("No ingresaste la longitud para recortar el texto")
: console.info(cadena.slice(0,longitud));

recortarTexto("Hola mundo",4);
recortarTexto();
recortarTexto("Hola mundo");
recortarTexto("", 5);