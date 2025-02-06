package main

// 1
// EL FAMOSO "FIZZ BUZZ"
/*
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
*/

import (
	"fmt"
)

func main() {
	
	fizzBuzz()
	
}

func fizzBuzz() {

	var rangeNum int = 100

	for i := 1; i <= rangeNum; i++ {
		if i % 3 == 0 && i % 5 == 0 {

		} else if i % 3 == 0 {
			fmt.Println("fizz")
		} else if i % 5 == 0 {
			fmt.Println("buzz")
		} else {
			fmt.Println(i)
		}
	} 
}