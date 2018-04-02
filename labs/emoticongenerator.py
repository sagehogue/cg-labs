

from random import choice

eyes_list = [ ';', '=', '8', '>:', 'x', 'X']
nose_list = ['^', '-', ':']
mouth_list = ['D', 'd', 'P', 'p', '*', 'O', ']', '[', ')', '(', '#', '@']

i = 1

while i in range(1, 6):
    s_eyes = choice(eyes_list)
    s_nose = choice(nose_list)
    s_mouth = choice(mouth_list)
    print("{}{}{}".format(s_eyes, s_nose, s_mouth))
    i = i + 1
