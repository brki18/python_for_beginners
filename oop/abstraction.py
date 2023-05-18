class Player:
    _private_var = 'test'

    def __init__(self, name, type, weapon):
        self.name = name
        self.type = type
        self.weapon = weapon

    def attack(self):
        print(f'{self.name} the {self.type} attacked with {self.weapon}')


wizard = Player('Merlin', 'wizard', 'magic')
archer = Player('Robin Hud', 'archer', 'bow')

# wizard.attack = 'Changed to string'

# print(wizard.attack)

# wizard.attack()
# archer.attack()

print(len([1, 2, 34]))


def player_attack(player):
    player.attack()

# player_attack(wizard)
# player_attack(archer)
