class Cars:
    def __init__(self, color, doors):
        self.wheelsnum = 4
        self.doorsnum = doors
        self.color = color

    def honk(self):
        print('{} honks: honk HONK'.format(self))
