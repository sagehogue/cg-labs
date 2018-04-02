#calculator allowing for numerical calculation and supporting alphanumeric translation for 1 through 20.

from string import ascii_letters

def get_operation():
    return input('What operation would you like to perform?\n: ')

def get_nums():
    return input('What is the first number?\n: '), input('What is the second number?\n: ')

def display_res(numberone, optype, numbertwo, sum):
    print('{} {} {} = {}'.format(numberone, optype, numbertwo, sum))

def again():
    return input('Would you like to make another calculation? y/n\n: ')

def formatting(alpha1, alpha2):
    alphalist1 = alpha1.split()
    alphalist2 = alpha2.split()
    numeric1 = []
    numeric2 = []
    for i in alphalist1:
        numeric1.append(alphatonumeric[i])
    for i in alphalist2:
        numeric2.append(alphatonumeric[i])
    return numeric1, numeric2

def determine_comptype(optype, num1, num2):
    if type_of_op == '+':
        sum1 = num1 + num2
        return sum1
    elif type_of_op == '-':
        sum1 = num1 - num2
        return sum1
    elif type_of_op == '*':
        sum1 = num1 * num2
        return sum1
    elif type_of_op == '/':
        sum1 = num1 / num2
        return sum1

def listtoint(list1, list2):
    val1 = 0
    val2 = 0
    for i in list1:
        val1 += int(i)
    for i in list2:
        val2 += int(i)
    return val1, val2


while True:
    alphatonumeric = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6,
    'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10, 'eleven': 11,
    'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15,
    'sixteen': 16, 'seventeen': 17, 'eighteen': 18, 'nineteen': 19, 'twenty': 20
    }
    type_of_op = get_operation()
    number1, number2 = get_nums()
    if number1[:1] in ascii_letters:
        num_list1, num_list2 = formatting(number1, number2)
        number1, number2 = listtoint(num_list1, num_list2)
    else:
        number1 = float(number1)
        number2 = float(number2)
    oursum = determine_comptype(type_of_op, number1, number2)
    display_res(number1, type_of_op, number2, oursum)
    conf = again()
    if conf == 'n' or conf == 'no':
        exit()
    else:
        continue
