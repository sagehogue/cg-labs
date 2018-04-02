#gradinglab v2

g_num = int(input('Please type your numerical grade\n: '))
plus_minus = (g_num % 10)

if plus_minus >= 7:
    plus_minus = "+"
elif plus_minus <= 3:
    plus_minus = "-"
else plus_minus = ""

if g_num > 89:
    print('You got an A' + plus_minus + "!")
elif g_num >= 80:
    print('You got a B' + plus_minus + "!")
elif g_num >= 70:
    print('You got a C' + plus_minus + "!")
elif g_num >= 60:
    print('You got a D' + plus_minus + "!")
elif g_num >= 50:
    print('You got a F' + plus_minus + "!")
else:
    print('You incorrectly input your grade or you got a terrible one.')
