/*
Programa una funcion que obtenga un numero aleatorio entre 501 y 600 */

function aleatorio1(min, max) {
    return Math.floor(Math.random() * (max - min + 1) + min);
  }

// for(let i = 0; i <= 10; i++){
//     console.log(aleatorio(501,600))
// }

//\/\/\\/\/\/\/\/\/\/\\/\/\/\/\/\/\/\/\/\/\/\\/\

const aleatorio = () => console.info(Math.round((Math.random() * 100) + 500) );

aleatorio()