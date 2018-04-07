
import random
from user import User
from enemy import Enemy


def checktile(i, j):  # Checks for content in tile
    return bool(board[i][j])


def placeobj(obj, i=0, j=0):  # places a single instance of object or symbol
    if i == 0 and j == 0:
        while True:
            gen_i = random.randint(0, height - 1)
            gen_j = random.randint(0, width - 1)
            if checktile(gen_i, gen_j) is False:
                board[gen_i][gen_j] = obj
                break
    else:
        gen_i = i
        gen_j = j
        board[gen_i][gen_j] = obj



width = 25  # the width of the board - rep by j
height = 25  # the height of the board - rep by i
mincoord = 0
maxcoord = height
u_spawn_i = 3
u_spawn_j = 3
# create a board with the given width and height
# we'll use a list of list to represent the board
board = []  # start with an empty list
for row in range(height):  # loop over the rows - row = 0 in range 0-49
    board.append([])  # append an empty row - board[0] = ''
    for column in range(width):  # loop over the columns - col = 0 in range 0-49
        board[row].append(' ')  # append an empty space to the board - board[0][0] = ''

for wall in range(0, height-1):
    board[wall][0] = '⍉'
    board[0][wall] = '⍉'
    board[24][wall] = '⍉'
    board[wall][24] = '⍉'

# define the player position
# add 4 enemies in random locations
snakeman_list = []
for count in range(4):
    snakeman = Enemy('Snake Man', '§', 5, 2)
    snakeman_list.append(snakeman)
    placeobj(snakeman_list[-1])


placeobj('⌘', 12, 12)

print('Welcome to Sagelandia!')  # intro screen
print('')
username = input('What is your character\'s name?: \n')
print('')
print('')
print('Welcome {}!\nWASD for directional control, enter "done" to exit.'.format(username))
user = User(username, u_spawn_i, u_spawn_j, mincoord, maxcoord)
# loop until the user says 'done' or dies
while True:
    command = input('> ')  # get the command from the user
    if command == 'done':
        break  # exit the game
    elif command in 'wasd':
        user.move(command)
    else:
        print('I did not understand that command.\n')

    # check if the player is on the same space as an enemy
    if board[user.loci][user.locj] == '§':
        print('you\'ve encountered an enemy!')
        action = input('what will you do? ')
        if action == 'attack':
            print('you\'ve slain the enemy')
            board[user.loci][user.locj] = ' '  # remove the enemy from the board
        else:
            print('you hestitated and were slain')
            break
    print("\n" * 50)
    print(user.loci, user.locj)
# define player visibility for fog of war
    visible_height = range(user.loci - 4, user.loci + 4)
    visible_width = range(user.locj - 4, user.locj + 4)
    for it in range(height):
        for jit in range(width):
            # if we're at the player location, print the player icon
            if it == user.loci and jit == user.locj:
                print('☺', end='')
            else:
                # if it in visible_height and jit in visible_width:
                if it in visible_height and jit in visible_width:
                    print(board[it][jit], end='')  # otherwise print the board square
        print()

