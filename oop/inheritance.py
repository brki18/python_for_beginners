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

    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon

    def attack(self):
        print(f'{self.name} is attacking with {self.weapon}')


wizard1 = Wizard('Merlin', 'magic')
archer1 = Archer('Robin Hud', 'bow')

# wizard1.attack()
# wizard1.sign_in()
#
# print(type(wizard1))

print(wizard1.__doc__)
print(isinstance(wizard1, Wizard))
print(isinstance(wizard1, Player))
print(isinstance(wizard1, object))
