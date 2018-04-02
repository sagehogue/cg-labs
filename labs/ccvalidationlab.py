def get_ccn():
    return input('Enter your ccn.\n\n: ')

def ccn_list(given_ccn):
    ccn_lst = []
    for i in given_ccn:
        ccn_lst.append(int(i))
    chkdig = ccn_lst.pop()
    return ccn_lst, chkdig

ccn_unprep = get_ccn()
# print(ccn_unprep)
# ccn_strlist = list(ccn_unprep[])
# unneededpop = ccn_strlist.pop()
the_ccn_list, checkdigit = ccn_list(ccn_unprep)
the_ccn_list.reverse()
# print(reversed_list)
# ccn_strlist = list(map(str(), the_ccn_list))
for i in len(the_ccn_list)[::2]:
    cur_dig = (the_ccn_list[i] * 2)
    if cur_dig >= 10:
        cur_dig = cur_dig - 9
    the_ccn_list[i] = cur_dig
num_sum = 0
for indice in len(the_ccn_list):
    num_sum += the_ccn_list[indice]
if num_sum[1] == checkdigit:
    print('Your ccn has been successfully validated!')
else:
    print('Your ccn is invalid. ;(')
# Convert the input string into a list of ints
# Slice off the last digit. That is the check digit.
# Reverse the digits.
# Double every other element in the reversed list.
# Subtract nine from numbers over nine.
# Sum all values.
# Take the second digit of that sum.
# If that matches the check digit, the whole card number is valid.

# 4556737586899855
