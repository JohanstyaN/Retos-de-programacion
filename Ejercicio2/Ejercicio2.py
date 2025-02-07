# 2
# ¿ES UN ANAGRAMA?
'''
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
'''

def is_anagram(word1, word2):
    if word1 == word2:
        return False
    return sorted(word1) == sorted(word2)

def is_anagram_analog(word1, word2):
    if word1 == word2:
        return False
    
    word1 = list(word1)
    word2 = list(word2)
    
    for letter in word2:
        if letter in word1:
            word1.remove(letter)
        else:
            return False
    
    return True

def is_anagram_analog2(word1, word2):
    if word1 == word2:
        return False
    
    word1 = list(word1)
    word2 = list(word2)
    
    for letter in word2:
        try:
            word1.remove(letter)
        except:
            return False
    
    return True

def is_anagram_analog3(word1, word2):
    
    if word1 == word2:
        return False
    
    def count_letters(word):
        letters = {}
        for letter in word:
            if letter in word:
                letters[letter] = letters.get(letter, 0) + 1
        return letters
    
    return count_letters(word1) == count_letters(word2)

# Tests
# is_anagram
print("1 Solution")
print(is_anagram("amor", "roma")) # True
print(is_anagram("amor", "amor")) # False
print(is_anagram("amor", "mora")) # True
print(is_anagram("amor", "moro")) # False
print(is_anagram("amor", "mor")) # False
print(is_anagram("amor", "mora")) # True
# is_anagram_analog
print("2 Solution")
print(is_anagram_analog("amor", "roma")) # True
print(is_anagram_analog("amor", "amor")) # False
print(is_anagram_analog("amor", "mora")) # True
# is_anagram_analog2
print("3 Solution")
print(is_anagram_analog2("amor", "roma")) # True
print(is_anagram_analog2("amor", "amor")) # False
print(is_anagram_analog2("amor", "mora")) # True
# is_anagram_analog3
print("4 Solution")
print(is_anagram_analog3("amor", "roma")) # True
print(is_anagram_analog3("amor", "amor")) # False
print(is_anagram_analog3("amor", "mora")) # True