#no more weather numbaguessav1
import random

def determine_num():
    return random.randint(1, 100)

def user_guess(guess_tally_int):
    guess_tally_int += 1
    return int(input('Guess the number(1-100)\n: ')), guess_tally_int

def eval_guess(guess_2_eval, guess_goal, guess_tally_thing):
    if guess_2_eval == guess_goal:
        print('You did it! The number was {} and you guessed it in {} guess(es)! Mad congratz.'.format(guess_goal, guess_tally_thing))
        pass
    elif guess_2_eval > guess_goal:
        print('Oops! {} is higher than the number! You have guessed {} time(s).'.format(guess_2_eval, guess_tally_thing))
    elif guess_2_eval < guess_goal:
        print('Oops! {} is lower than the number! You have guessed {} time(s)'.format(guess_2_eval, guess_tally_thing))

def guess_delta(last_guess, present_guess, target):
    last_diff = abs(last_guess - target)
    current_diff = abs(present_guess - target)
    if last_diff > current_diff:
        print('\nYour guess was closer than last time!\n')
    elif last_diff < current_diff:
        print('\nThis guess was even further off!\n')
    elif last_diff == current_diff:
        print('\nDang, no closer or further than your last guess..\n')

def again():
    return input('Would you like play again?\n: ')


while True:
    comp_num = determine_num()
    i = 0
    current_guess = 0
    prev_guess = 0
    guess_tally = 0
    while True and current_guess != comp_num:
        current_guess, guess_tally = user_guess(guess_tally)
        eval_guess(current_guess, comp_num, guess_tally)
        if prev_guess != 0 and current_guess != comp_num:
            guess_delta(prev_guess, current_guess, comp_num)
        prev_guess = current_guess
    user_conf = again()
    if user_conf in 'y' or user_conf in 'yes':
        continue
    else:
        quit()
