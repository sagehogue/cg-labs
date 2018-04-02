

def greeting():
    print('Welcome to your fancy phone number formatting program!\n\n\n')

def get_phonenumber():
    phonenumber = input('Lemme format yo phone number, gimme just the digits.\n: ')
    return phonenumber

def format_number(input_number):
    # i = 0
    # beginning = ""
    # middle = ""
    # end = ""
    nlist = list(input_number)
    beginning = '('+ nlist[0] + nlist[1] + nlist[2] + ')'
    middle = nlist[3] + nlist[4] + nlist[5] + '-'
    end = nlist[6] + nlist[7] + nlist[8] + nlist[9]
    return beginning, middle, end


def display_phonenumber(beg, mid, en):
    print("Your fancy new formatted phone number is {}{}{}".format(beg, mid, en))

greeting()
user_number = get_phonenumber()
area, mid_bit, end_bit = format_number(user_number)
display_phonenumber(area, mid_bit, end_bit)
