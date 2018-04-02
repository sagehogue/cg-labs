#v2
import random


adjectives = input("Give me three adjectives separated by commas and spaces.\n: ")
adj1,adj2,adj3 = adjectives.split(", ")
nouns = input("Give me three nouns separated by commas and spaces.\n: ")
n1,n2,n3 = nouns.split(', ')
noun_list = [n1, n2, n3]

print("Oh my {}! I see a most {} {}. What a {} day it is, and a {} existence to boot. Oh, I don't know, what do you think {}?").format(random.Choice(noun_list), adj1, random.Choice(noun_list), adj2, adj3, random.Choice(noun_list))

#this last line doesn't run for some reason - claims it isn't an appropriate data type for .format
