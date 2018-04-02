

def get_width():
        return int(input('What is the width of your wall in feet?\n: '))

def get_height():
        return int(input('What is the height of your wall in feet?\n: '))

def get_coats():
        return int(input('How many coats of paint?\n: '))

def get_price():
    while True:
        return int(input('What is the price of a gallon of paint in cents?'))

def get_footage(i_wid, i_height, coats, more_width, more_height):
    footage = (((i_wid * i_height) + (more_width * more_height)) * coats)
    return footage

def get_paintnum(footage):
    paintcans = (footage // 400)
    if (footage / 400) != 0:
        paintcans += 1
    return paintcans

def get_cost(paintcans, price):
    cost = ((paintcans * price) / 100)
    return cost

def display(paint, price):
    return('You will need ' + str(paint) + ' cans of paint and it will cost you ' + str(price) + ' dollars.')


w_width = get_width()
more_width = 0
w_height = get_height()
more_height = 0
p_price = get_price()
coat_num = get_coats()
while True:
    morewalls = input('Would you like to add more dimensions? (y/n)\n: ').lower()
    if morewalls == 'y':
        more_width = get_width()
        more_height = get_height()
    elif morewalls == 'n':
        pass
    else:
        morewalls = input('Would you like to add more dimensions? (y/n)\n: ').lower()
    footage = get_footage(w_width, w_height, coat_num, more_width, more_height)
    paintcans = get_paintnum(footage)
    cost = get_cost(paintcans, p_price)
    print(display(paintcans, cost))
    quit()
