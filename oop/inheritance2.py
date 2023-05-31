class Player:

    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('User is logged in')


class Wizard(Player):

    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon

    def attack(self):
        print(f'{self.name} is attacking with {self.weapon} with power level {self.power_level}')


class Archer(Player):

    def __init__(self, name, weapon, email):
        super().__init__(email)
        self.name = name
        self.weapon = weapon

    def attack(self):
        print(f'{self.name} is attacking with {self.weapon}')


# super keyword
archer = Archer('John', 'bow', 'john@gmail.com')

# print(archer.email)

# Object introspection
print(dir(archer))
