#rpslab.py


from random import choice


rps_dict = {"rock" : ["scissors", "paper"], "paper" : ["rock", "scissors"], "scissors" : ["paper", "rock"]}
rps_list = ["rock", "paper", "scissors"]
def ask_user():
    return input('Rock, paper, or scissors?: ').lower()

def ask_comp():
    return choice(rps_list)

def evaluate():
    if comp_move == (rps_dict[user_move][0]):
        return ('You picked ' + user_move + ' and I picked ' + comp_move + ' so you win! Congratumuckations.')
    elif comp_move == (rps_dict[user_move][1]):
        return ('You picked ' + user_move + ' and I picked ' + comp_move + ' so you lose! Hahahaha!')
    else:
        return ('You picked ' + user_move + ' and I picked ' + comp_move + '! A friggin tie can you believe it?!')

def permission():
    return input('Would you like to play? (yes/no)\n: ').lower()


user_permission = permission()

while user_permission == 'yes':
    user_move = ask_user()
    while user_move not in rps_list:
        user_move = input('Rock, paper, or scissors?: ').lower()
    comp_move = ask_comp()
    print(evaluate())
    user_permission = permission()
