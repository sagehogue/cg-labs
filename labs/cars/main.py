from cars import Cars

#figured it out in the coolcars statement - need to fix the other ones though

cool_car = Cars('Red', '2')
lame_car = Cars('Brown', '4')
great_car = Cars('Green', '4')

great_car.honk()
print('Information for cool car: color: {}, number of doors: {}\nInformation for lame car: color: {}, number of doors: {}\nInformation for great car: color: {}, number of doors: {}'.format(cool_car.color, cool_car.doorsnum, lame_car.color, lame_car.doorsnum, great_car.color, great_car.doorsnum))
