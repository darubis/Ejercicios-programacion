#!/bin/bash

# Programa una función que obtenga un número aleatorio entre 501 y 600

numero_random() {
  echo $(shuf -i 501-600 -n 1)
}

for i in {1..10}; do
  numero_random
done