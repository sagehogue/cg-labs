#gradinglab.py v1

g_num = int(input('Please type your numerical grade\n: '))

if g_num > 89:
    print('You got an A!')
elif g_num >= 80:
    print('You got a B!')
elif g_num >= 70:
    print('You got a C!')
elif g_num >= 60:
    print('You got a D!')
elif g_num >= 0:
    print('F! Retake that or tank your grade. :(')
else:
    print('Oops! You failed the test of "Can I successfully input a numerical value?"')
    g_num = input('Please type your numerical grade\n: ')
