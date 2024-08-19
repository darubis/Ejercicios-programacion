/* Programa una funcion que cuente el numero de caracteres de una cadena de texto. 
miFuncion("Hola mundo") devolvera 10 */

// funcion declarada 

// function contarCaracteres(cadena=""){
//     if (!cadena){
//         console.warn("No ingresaste ninguna cadena");
//     }else{
//         console.info(`La cadena "${cadena}" tiene ${cadena.length} caracteres`);
//     }
// }


// funcion expresada

const contarCaracteres = (cadena="") => 
(!cadena)
? console.warn("No ingresaste ninguna cadena")
: console.info(`La cadena "${cadena}" tiene ${cadena.length} caracteres`);


contarCaracteres();
contarCaracteres("Hola mundo");