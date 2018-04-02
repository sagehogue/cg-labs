#palindromes simple


from string import punctuation

def get_string():
    return input('Is it a palindrome?\n: ')

def rid_space(stringo):
    for var in stringo:
        fofingo = stringo.replace(punctuation, '')
    print(fofingo)
    return fofingo

def isitpal(bingo):
        dingo = bingo[::-1]
        if bingo == dingo:
            print('It do palindrome.')
        else:
            print("It don't palindrome.")

pal_string = get_string()
rid_space(pal_string)
isitpal(pal_string)
#def make_list(string):
#     return list(string)
#
#def l_reverse(list):
#     reverse.(list)
