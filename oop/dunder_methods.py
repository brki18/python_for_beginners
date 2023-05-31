class DunderTest:

    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print('Helloo')

    def __str__(self):
        print(f'Color is: {self.name}')


dunder = DunderTest('John')

dunder.say_hello()

dunder.__str__()
