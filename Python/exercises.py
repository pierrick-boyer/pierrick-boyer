# https://python.developpez.com/exercices/?page=Les-chaines-de-caracteres#Rechercher-un-caractere-particulier-dans-une-chaine-de-caracteres

import string


# Write a script that determines whether or not a string contains the character
def search_character(sentence: str, character: str):
    if character in sentence:
        result = sentence.count(character)
        return f"The {character} is present {result} times, in {sentence}"

    else:
        return False


# ----------------------------------------------------------------------------------------------------------------------


# Write a script that copies a string (into a new variable), inserting asterisks between the characters
def write_between(word: str):
    return '*'.join(word)

# ----------------------------------------------------------------------------------------------------------------------
