class User:
    def __init__(self, n):
        self.loc1 = 1
        self.loc2 = 1
        self.life = 10
        self.max = 10
        self.min = 0
        self.name = n

    def move(self, direction):
        if self.checklocation(direction) == True:


    def checklocation(self, direction):
        if direction in 'w' or direction in 's':
            if self.loc1 + 1 > self.max or self.loc1 -1 < 0:
                return False
            else:
                return True
        elif direction in 'a' or direction in 'd':
            if self.loc2 + 1 > self.max or self.loc2 - 1 < 0:
                return False
            else:
                return True
        else:
            print('That key does nothing for you.\n')
            return False
