/*
    Porgrama una funcion que elimine cierto patron de caracteres de un texto dado.
    miFuncion("xyz1 xyz2 xyz3 xyz4 xyz5") devolvera "1,2,3,4 y 5"    
*/

const eliminarCaracteres = (texto = "", patron = "") => 
(!texto)
? console.warn("No ingresaste un texto")
: (!patron)
? console.warn("No ingresaste un patron de caracteres")
: console.info(texto.replace(new RegExp(patron, "ig"), ""));


eliminarCaracteres();
eliminarCaracteres("xyz1 xyz2 xyz3 xyz4 xyz5");
eliminarCaracteres("xyz1 xyz2 xyz3 xyz4 xyz5","xyz");