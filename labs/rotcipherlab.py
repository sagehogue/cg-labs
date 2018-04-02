# stuck here couldn't figure out how to match the current iterable letter to the rotated one
from string import ascii_lowercase

def get_string():
    return input('Please enter the phrase...\n: ')

def en_or_de():
    return input('Would you like to encrypt or decrypt a string? (e/d)\n: ')

alpha_list = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g',
    'h', 'i', 'j', 'k', 'l', 'm', 'n',
    'o', 'p', 'q', 'r', 's', 't', 'u',
    'v', 'w', 'x', 'y', 'z', ' '
]
rot13list = [
    'n', 'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z', 'a',
    'b', 'c', 'd', 'e', 'f', 'g', 'h',
    'i', 'j', 'k', 'l', 'm', ' '
]
ende = en_or_de()
input_string = get_string().lower()
trans_term = ''

if ende.lower() in 'e':
    for i in input_string:
        indice = alpha_list.index(i)
        trans_term += rot13list[indice]
elif ende.lower() in 'd':
    for i in input_string:
        indice = rot13list.index(i)
        trans_term += alpha_list[indice]
print(trans_term)
