# avgnumlab.py - basicv - Now with less salt!

def basefunction():
    return input('Please enter numbers you wish you have averaged or type "done"\nTo quit enter q\n\n: ')


def do_math(raw_sum, the_list):
    dividing_num = len(the_list)
    completed_avg = raw_sum / dividing_num
    return completed_avg


def display_numbers(final_num, number_list):
    print('Array provided: {}\nResulting Average: {}'.format(number_list, final_num))


num_list = []
num_sum = 0
while True:
    returnvar = basefunction()
    if returnvar.isdigit() == True:
        var_toreturn = int(returnvar)
        num_list.append(var_toreturn)
        continue
    elif returnvar.lower() == 'done':
        sum = 0
        for iterator in num_list:
            sum += iterator
        final_sum = do_math(sum, num_list)
        display_numbers(final_sum, num_list)
        conf = input('Would you like you average another set?(y/n)\n: ').lower()
        if conf == 'y' or conf == 'yes':
            num_list = []
            continue
        elif conf == 'n' or conf == 'no':
            quit()
    elif returnvar.lower() == 'q' or returnvar.lower() == 'quit':
        exit()
    else:
        continue
