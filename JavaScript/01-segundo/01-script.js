/*
    Programa una funcion para contar el numero de veces que se repite una palabra
    en un texto largo. miFuncion("Hola mundo adios mundo", "mundo") devolvera 2
*/


const textoEnCadena = (cadena = "", texto = "") => {
    if (!cadena) return console.warn("No ingresaste el texto largo");
    
    if (!texto) return console.warn("No ingresaste la palabra a evaluar");

    let i = 0,
        contador = 0;

    while(i !== -1){
        i = cadena.indexOf(texto,i)
        if (i  !== -1){
            i++;
            contador++;
        }
    }

    return console.info(`La palabra ${texto} se repite ${contador} veces`)
}

textoEnCadena();
textoEnCadena("","mundo");
textoEnCadena("hola mundo adios mundo");
textoEnCadena("hola mundo adios mundo", "mundo")