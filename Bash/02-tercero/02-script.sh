#!/bin/bash

# Programa una función que reciba un número y evalúe si es capicúa o no

#!/bin/bash

# Función para verificar si un número es capicúa
function es_capicua() {
  local numero="$1"
  local inverso=""

  # Invierte el número convirtiéndolo a cadena y luego a arreglo
  for (( i=${#numero}-1; i>=0; i-- )); do
    inverso+="${numero:$i:1}"
  done

  # Compara el número original con su inverso
  if [[ "$numero" == "$inverso" ]]; then
    echo "El número $numero es capicúa"
  else
    echo "El número $numero no es capicúa"
  fi
}

# Solicita al usuario un número
read -p "Ingrese un número: " numero

# Llama a la función y muestra el resultado
es_capicua "$numero"