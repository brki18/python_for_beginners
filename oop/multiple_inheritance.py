class Player:
    power_level = 50

    def sign_in(self):
        print('User is logged in')


class Wizard(Player):

    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon

    def attack(self):
        print(f'{self.name} is attacking with {self.weapon} with power level {self.power_level}')


class Archer(Player):

    def __init__(self, name, weapon, arrows_num):
        self.name = name
        self.weapon = weapon
        self.arrows = arrows_num

    def attack(self):
        print(f'{self.name} is attacking with {self.weapon}')

    def shoot_arrows(self):
        print(f'Arrows remaining: {self.arrows}')


class Hybrid(Wizard, Archer):

    def __init__(self, name, weapon, arrows_num):
        Wizard.__init__(self, name, weapon)
        Archer.__init__(self, name, weapon, arrows_num)


hybrid = Hybrid('John', 'arrows', 100)

hybrid.attack()
hybrid.shoot_arrows()
