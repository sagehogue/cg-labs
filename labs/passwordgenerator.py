

from random import choice
from string import printable
def get_n():
    return input('Enter desired password length\n: ')
def get_char():
    return choice(printable)

n = int(get_n())

count = 1
password = ""
while count in range(1, (n + 1)):
    password += get_char()
    count += 1
print("Your randomly generated password is: " + password)
