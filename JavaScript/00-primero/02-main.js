/*Programa una funcion que dada una String te devuelva un Array de textos separados por 
cierto caracter. miFuncion("Hola que tal","") devolvera ["Hola", "que", "tal"] */

const cadenaAArreglo = (cadena = "", separador = undefined) =>
(!cadena)
? console.warn("No ingresaste una cadena de texto")
: (separador == undefined)
? console.warn("No ingresaste un separador")
: console.info(cadena.split(separador));

cadenaAArreglo("Lorem ipsum dolor sit, amet consectetur adipisicing elit. Repellendus velit enim nulla non officia harum eum rerum ullam. Repellat accusamus doloribus odit ducimus nesciunt. Accusantium magni saepe excepturi possimus doloremque.", " ");

cadenaAArreglo("Ene,Feb,Mar,Abr,May,Jun,Jul,Ago,Sep,Oct,Nov,Dic", ",");

cadenaAArreglo();
cadenaAArreglo("hola mundo");
cadenaAArreglo("","-");