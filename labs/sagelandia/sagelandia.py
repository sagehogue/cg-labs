import random
from user import User


def checktile(i, j): # Checks for content in tile
    return bool(board[i][j])


def placeobj(objsym, i=0, j=0): # places a single instance of object or symbol
    if i == 0 and j == 0:
        while True:
            gen_i = random.randint(0, height - 1)
            gen_j = random.randint(0, width - 1)
            if checktile(gen_i, gen_j) is False:
                board[gen_i][gen_j] = objsym
                break
    else:
        gen_i = i
        gen_j = j
        board[gen_i][gen_j] = objsym


width = 50  # the width of the board - rep by j
height = 50  # the height of the board - rep by i

# create a board with the given width and height
# we'll use a list of list to represent the board
board = []  # start with an empty list
for row in range(height):  # loop over the rows - row = 0 in range 0-49
    board.append([])  # append an empty row - board[0] = ''
    for column in range(width):  # loop over the columns - col = 0 in range 0-49
        board[row].append(' ')  # append an empty space to the board - board[0][0] = ''

for edge1 in board:
    edge1[0] = '|'
for edge2 in board[0]:
    edge2 = '*'


    # for side1 in range(len(board[0])):
    #     board[0][side1] = '|'
    # for side2 in range(len(board[49])):
    #     board[49][side2] = '|'


# define the player position
player_i: int = 1
player_j = 1
# visible_height = [player_i - 4, player_i + 4]
# visible_width = [player_j - 4, player_j + 4] - maybe can do these differently

# define player visibility for fog of war
visible_height = range(player_i - 4, player_i + 4)
visible_width = range(player_j - 4, player_j + 4)


# add 4 enemies in random locations
for i in range(4):
    enemy_i = random.randint(0, height - 1)
    enemy_j = random.randint(0, width - 1)
    board[enemy_i][enemy_j] = '§'



print('Welcome to Sagelandia!')
print('')
print('WASD for directional control, enter "done" to exit.')
print('')
print('')
username = input('What is your character\'s name?: \n')
user = User(username)
# loop until the user says 'done' or dies
while True:

    command = input('> ')  # get the command from the user

    if command == 'done':
        break  # exit the game

    elif command in 'wasd':
        user.move(command)

    else:
        print('I did not understand that command.\n')
    # elif command == 'a':
    #     player_j -= 1  # move left
    # elif command == 'd':
    #     player_j += 1  # move right
    # elif command == 'w':
    #     player_i -= 1  # move up
    # elif command == 's':
    #     player_i += 1  # move down

    # check if the player is on the same space as an enemy
    if board[player_i][player_j] == '§':
        print('you\'ve encountered an enemy!')
        action = input('what will you do? ')
        if action == 'attack':
            print('you\'ve slain the enemy')
            board[player_i][player_j] = ' '  # remove the enemy from the board
        else:
            print('you hestitated and were slain')
            break
    visible_height = range(player_i - 4, player_i + 4)
    visible_width = range(player_j - 4, player_j + 4)
    for i in visible_height:
        for j in visible_width:
            # if we're at the player location, print the player icon
            if i == player_i and j == player_j:
                print('☺', end=' ')
            else:
                print(board[i][j], end=' ')  # otherwise print the board square
        print()

