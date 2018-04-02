# fone numba and it aint working


def get_numba():
    fonenumba = input('Lemme format yo phone number, gimme just the numbers.')
    return fonenumba

def split_numba(fonenumba, area, mid, end):
    for area in range (0, fonenumba[3]):

    return areacode, middlebit, lastbit

def format_numba(area, mid, end):
    format_num = '(' + area + ') ' + mid + '-' + end
    return format_num

def return_num(format_num):
    print('Your formatted phone number is: ' + format_num)


numba = get_numba()
area, mid, end = split_numba(numba)
format_num = format_numba(area, mid, end)
return_num(format_num)
