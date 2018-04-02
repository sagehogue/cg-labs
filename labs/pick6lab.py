# Generate a list of 6 random numbers representing the winning tickets
# Start your balance at 0
# Loop 100,000 times, for each loop:
# Generate a list of 6 random numbers representing the ticket
# Subtract 2 from your balance (you bought a ticket)
# Find how many numbers match
# Add to your balance the winnings from your matches
# After the loop, print the final balance
import random

def pick_winning_nums():
    winning_array = []
    for i in range(0, 6):
        winning_array.append((random.randint(1, 99)))
    # print(winning_array)
    return winning_array

def generate_ticket(current_balance):
    current_balance -= 2
    ticket_nums = []
    for it in range (0, 6):
        ticket_nums.append((random.randint(1, 99)))
    # print(ticket_nums, current_balance)
    return ticket_nums, current_balance

def calc_matches(winning_numset, cur_ticket, num_matchlist):
    # function_cur_ticket = cur_ticket
    # function_winset = winning_numset
    for iterator in range(len(winning_numset)):
        if winning_numset[iterator] == cur_ticket[iterator]:
            num_matchlist.append(winning_numset[iterator])
            # print(num_matchlist)
    return num_matchlist

# def calc_winnings(matching_numlist, user_balance, largest_win):
#         if len(matching_numlist) == 0 or 'None':
#             user_balance += 0
#             if largest_win == 0:
#                 largest_win = 0
#             return user_balance, largest_win
#         elif len(matching_numlist) == 1:
#             user_balance += 4
#             if largest_win <= 4:
#                 largest_win = 4
#             return user_balance, largest_win
#         elif len(matching_numlist) == 2:
#             user_balance += 7
#             if largest_win <= 7:
#                 largest_win = 7
#             return user_balance, largest_win
#         elif len(matching_numlist) == 3:
#             user_balance += 100
#             if largest_win <= 100:
#                 largest_win = 100
#             return user_balance, largest_win
#         elif len(matching_numlist) == 4:
#             user_balance += 50000
#             if largest_win <= 50000:
#                 largest_win = 50000
#             return user_balance, largest_win
#         elif len(matching_numlist) == 5:
#             user_balance += 1000000
#             if largest_win <= 1000000:
#                 largest_win = 1000000
#             return user_balance, largest_win
#         elif len(matching_numlist) == 6:
#             user_balance += 25000000
#             if largest_win <= 25000000:
#                 largest_win = 25000000
#             return user_balance, largest_win
#         else:
#             raise ValueError

def calc_winnings(the_balance, matching_numlist):
    calc_bal = the_balance
    calc_bal += balance_table[len(matching_numlist)]

    return calc_bal

def calc_largest_win(largest_win, matchlista):
    if largest_win < balance_table[len(matchlista)]:
        largest_win = balance_table[len(matchlista)]
    return largest_win

def display(lucky_array, final_balval, lrgst_winzo):
    print()
    print('The lucky array was: {}'.format(lucky_array))
    print('After 100,000 attempts at playing the lottery, your balance is...')
    print()
    print('{}!!! Your largest single win was {}'.format(final_balval, lrgst_winzo))
    print()

def playagain():
    return input('Play again? (y/n)\n: ').lower()

balance_table = {0: 0, 1: 4, 2: 7, 3: 100, 4: 50000, 5: 1000000, 6:25000000}
while True:
    i = 0
    balance = 0
    big_win = 0
    winning_nums = pick_winning_nums()
    while i in range(0, 100000):
        num_matches = []
        current_ticket, balance = generate_ticket(balance)
        found_matches = calc_matches(winning_nums, current_ticket, num_matches)
        balance = calc_winnings(balance, found_matches)
        big_win = calc_largest_win(big_win, found_matches)
        # balance, big_win = calc_winnings(found_matches, balance, big_win)
        i += 1
    display(winning_nums, balance, big_win)
    consent = playagain()
    if consent == 'y' or consent == 'yes':
        continue
    elif consent == 'no' or consent == 'n':
        exit()
