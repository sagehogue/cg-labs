class User:
    def __init__(self, n):
        self.loc1 = 1
        self.loc2 = 1
        self.life = 10
        self.max = 49
        self.min = 0
        self.name = n

    def move(self, direction):
        if self.checklocation(direction) is True:
            if direction in 'w':
                self.loc1 -= 1  # move up
                print(self.loc1, self.loc2)
            elif direction in 's':
                self.loc1 += 1  # move down
                print(self.loc1, self.loc2)
            elif direction in 'a':
                self.loc2 -= 1
                print(self.loc1, self.loc2)
            elif direction in 'd':
                self.loc2 += 1
                print(self.loc1, self.loc2)
        elif self.checklocation(direction) is False:
            print("You can't go that way!")

    def checklocation(self, direction):
        if direction in 'w' or direction in 's': #gotta split conditionals up for specificity - cant move down if im too close to top border rn
            if self.loc1 + 1 >= self.max or self.loc1 - 1 <= self.min:
                return False
            else:
                return True
        elif direction in 'a' or direction in 'd':
            if self.loc2 + 1 >= self.max or self.loc2 - 1 <= self.min:
                return False
            else:
                return True
        else:
            print('That key does nothing for you.\n')
            return False

if __name__ == '__main__':
    username = input('What is your character\'s name?: \n')
    user = User(username)