# pig latin most advanced

import string

def getword():
    return str(input('Give me something to piglatinify!\n: '))

def make_latin(nonlatin_word):
    if nonlatin_word[0].lower() in vowel_list:
        returnword = nonlatin_word + "yay"
        return returnword
    else:
        nonlatin_wordloopv = nonlatin_word
        initial_consonants = ""
        alatin_list = list(nonlatin_word)
        while alatin_list[0] not in vowel_list:
            initial_consonants += alatin_list.pop(0)
            # nonlatin_wordloopv.pop(0)
        morelatin_word = ''.join(alatin_list) + initial_consonants + "ay"
        return morelatin_word

def fix_capitalization(original_word, wordtobefixed):
    if original_word[0].isupper() == True:
        wordbeenfixed = wordtobefixed.capitalize()
        return wordbeenfixed
    else:
        wordbeenfixed = wordtobefixed.lower()
    return wordbeenfixed


def display_latin(nonlatin, piglatin):
    print('{} in pig latin is {}.'.format(nonlatin, piglatin))

vowel_list = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U', 'Y', 'y']
consonant_list = []
for consonant in string.ascii_lowercase:
    if consonant not in vowel_list:
        consonant_list.append(consonant)

nontransformed = getword()
transformed = make_latin(nontransformed)
final_formation = fix_capitalization(nontransformed, transformed)
display_latin(nontransformed, final_formation)
