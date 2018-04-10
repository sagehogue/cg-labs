from random import choice


class User:
    def __init__(self, n, playeri, playerj, minimum=0, maximum=49):
        self.loci = playeri
        self.locj = playerj
        self.life = 10
        self.max = maximum
        self.min = minimum
        self.name = n

    def move(self, direction):
        if self.checklocation(direction) is True:
            if direction in 'w':
                self.loci -= 1  # move up
                # print(self.loci, self.locj)
            elif direction in 's':
                self.loci += 1  # move down
                # print(self.loci, self.locj)
            elif direction in 'a':  # move left
                self.locj -= 1
                # print(self.loci, self.locj)
            elif direction in 'd':  # move right
                self.locj += 1
                # print(self.loci, self.locj)
        elif self.checklocation(direction) is False:
            print("You can't go that way!")

    def checklocation(self, direction):
        if direction in 'w':  # Gotta make sure a and d max/min params set correctly
            if self.loci - 1 <= self.min:
                return False
            else:
                return True
        elif direction in 's':
            if self.loci + 1 >= self.max - 1:
                return False
            else:
                return True
        elif direction in 'a':
            if self.locj - 1 <= self.min:
                return False
            else:
                return True
        elif direction in 'd':
            if self.locj + 1 >= self.max - 1:
                return False
            else:
                return True
        else:
            print('That key does nothing for you.\n')
            return False

    def take_damage(self, quantity, causeofdeath=None):
        print('Agh! {} takes {} damage!'.format(self.name, quantity))
        if self.life - quantity >= 1:
            self.life -= quantity
        elif self.life - quantity <= 0:
            self.to_valhalla(causeofdeath)

    def to_valhalla(self, cod):
        wod_list = [
            'eviscerated', 'brought into the cold embrace of death', 'totally destroyed', 'utterly crushed',
            'disgustingly annihilated', 'made into shreds', 'pulped', 'creamed', 'defenestrated', 'decapitated',
            'lethally abused', 'gutrocked', 'taken to the farm', 'flushed down the toilet', 'brought upstate',
            'lugied out', 'put in the ground', 'turned into gorenamentation'
        ]
        if cod is None:
            print('{} feels the cold embrace of death'.format(self.name))
            exit()
        else:
            print('{} was {} by {}'.format(self.name, choice(wod_list), cod))
            exit()