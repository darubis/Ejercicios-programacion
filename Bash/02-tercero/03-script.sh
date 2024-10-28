#!/bin/bash

# Función para calcular el factorial de manera iterativa
function factorial_iterativo() {
  local n=$1
  local answer=1

  for ((i = 2; i <= n; i++)); do
    answer=$((answer * i))
  done

  echo $answer
}

# Función para calcular el factorial de manera recursiva con memoización
declare -A memo

function factorial_recursivo() {
  local n=$1

  # Si el valor está en el memo, devolverlo
  if [ -n "${memo[$n]}" ]; then
    echo "${memo[$n]}"
    return
  fi

  # Caso base
  if [ "$n" -eq 1 ]; then
    echo 1
    return
  fi

  # Recursión, capturando el valor de la llamada recursiva en una variable
  local result=$((n * $(factorial_recursivo $((n - 1)))))
  memo[$n]=$result
  echo $result
}

# Valor de n
n=20  # Usamos un número más pequeño para evitar problemas de recursión y límite de enteros

# Medición de tiempo para el factorial iterativo
echo "Factorial iterativo:"
time factorial_iterativo $n > /dev/null

# Medición de tiempo para el factorial recursivo
echo "Factorial recursivo:"
time factorial_recursivo $n > /dev/null