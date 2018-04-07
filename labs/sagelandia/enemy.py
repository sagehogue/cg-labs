from random import choice


class Enemy:
    def __init__(self, name, symbol, life, attack):
        self.name = name
        self.board_symbol = symbol  # plan to use § - perhaps I shall call him Snakeman!
        self.life = life
        self.attack = attack
        self.deathmessage = 'You have slain {}!'.format(self.name)

    def battle(self, user):
        while self.life >= 1 and user.life >= 1:
            self.user_turn(user)
            user.take_damage(self.make_attack(user), self.name)
        # if self.life <= 0:
        #     self.die_ingloriously(user)

    def user_turn(self, user):
        q = input('{}\' turn.\nWould you like to (a)ttack or access your (i)nventory?\n> '.format(user.name)).lower()
        if q in 'a' or q in 'i':  # haven't yet developed an inventory system
            self.take_dmg(user.attack, user)
        else:
            self.take_dmg(user.attack, user)

    def survives_hit(self, hit_taken):
        if self.life - hit_taken >= 1:
            return True
        else:
            return False

    def make_attack(self, targ_obj):
        print('{} makes an attack!'.format(self.name))
        return self.attack

    def take_dmg(self, dmg_taken, user):
        if self.survives_hit(dmg_taken) is True:
            self.life -= dmg_taken
            print('{} took {} damage!'.format(self.life, dmg_taken))
        elif self.survives_hit(dmg_taken) is False:
            self.die_ingloriously(user)

    def die_ingloriously(self, cod):
        wod_list = [
            'righteously cast down', 'brutally brought down', 'made into a sad meat patty',
            'converted into a puddle of flesh' 'bagged up like Canadian milk', 'given no fair trial',
            'given a sharp lesson to', 'beaten like a pinata'
        ]
        print('{} was {} by {}'.format(self.name, choice(wod_list), cod))

