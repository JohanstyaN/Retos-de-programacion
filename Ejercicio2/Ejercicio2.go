package main

import (
	"fmt"
	"sort"
)

// 2
// ¿ES UN ANAGRAMA?
/*
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
 */

func main() {

	fmt.Println(validate_anagram("roma", "amor"))
	fmt.Println(validate_anagram("roma", "amor1"))
	fmt.Println(validate_anagram("roma", "amor2"))
	fmt.Println(validate_anagram("roma", "mora"))
}

func convert(word1 string) []rune {

	runes := []rune(word1)

	sort.Slice(runes, func(i, j int) bool {
		return runes[i] < runes[j]
	})

	return runes
}

func validate_anagram(word1 string, word2 string) bool {

	if word1 == word2 {
		return false
	}

	if len(word1) != len(word2) {
		return false
	}

	runes1 := convert(word1)
	runes2 := convert(word2)

	for i := 0; i < len(runes1); i++ {
		if runes1[i] != runes2[i] {
			return false
		}
	}

	return true
}
