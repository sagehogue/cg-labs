#I guess I did all this... easy but a waste huh
from random import choice

def getnoun():
    got_noun = input('Give me a noun.\n: ')
    noun_list.append(got_noun)

def getadj():
    got_adj = input('Give me a adj.\n: ')
    adj_list.append(got_adj)

def getverb():
    got_verb = input('Give me a verb.\n: ')
    verb_list.append(got_verb)

def display_libs():
    print('It was a {} March day, the {} were singing in the trees and the {} {} were to be seen {}ing by the dozen.'.format(choice(adj_list), choice(noun_list), choice(adj_list), choice(noun_list), choice(verb_list)))

def user_confirmation():
    print()
    print('That was your madlibs!')
    print()
    return input('Would you like to play again? (y/n)\n: ')
noun_list = []
adj_list = []
verb_list = []

while True:
    getnoun()
    getadj()
    getverb()
    display_libs()
    permission = user_confirmation()
    if permission in 'y':
        continue
    if permission in 'n':
        exit()
