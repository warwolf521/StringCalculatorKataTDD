# TDD-String Calculator

Tarea realizada en python, usando el framework de testeo PyTest.\

Se realizo un par de commit o mas por cada paso solicitado en el ejercicio de Kata, en cada uno se explicita primero el conjunto de test a lograr, para posteriormente resolver estos mediante la implementacion minima para esto.

## Pasos:

**Paso 1:** Crea una simple calculadora de cadena de caracteres usando el siguiente modelo:

` int Add(string numbers)`

El metodo puede tomar hasta 2 numeros, separado por comas y debera retornar su suma.

**Paso 2:** Permite que el metodo maneje una cantidad desconocida de numeros

**Paso 3:** Permite que el metodo maneje `\n` entre los numeros (en vez de comas)

**Paso 4:** Soporte de diferentes delimitadores usando la siguiendo la siguiente forma: `“//[delimiter]\n[numbers…]”`

**Paso 5:** Llamar Add con un numero negativo ha de retornar la siguiente excepcion `"negatives not allowed"` y los negativos correspondientes en el cuerpo de la excepcion

**Paso 6:** Numeros mas grandes de 1000 han de ser ignorados

**Paso 7:** Delimitadores pueden tener cualquier largo con el siguiente formato: `“//[delimiter]\n”`

**Paso 8:** Permite multiple delimitadores de la siguiente forma: `“//[delim1][delim2]\n”`

**Paso 9:** Permite que los multiples delimitadores puedan tener largos mayor que uno.