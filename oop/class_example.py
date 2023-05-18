'''
1. Encapsulation
2. Abstraction
3. inheritance
4. Polymorphism
'''


class User:
    age = 40

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def login(self, username, password):
        print(f'{username}, You are logged in')

    @classmethod
    def class_method(cls):
        print(cls.age)
        print('This is class method')

    @staticmethod
    def static_method():
        print('This is static method')


User.static_method()
User.class_method()
# User.login('asd', 'asd')

user1 = User('Marko', 'brki@gmail.com')
user2 = User('John', 'john@live.com')

# print(user1.email)
# print(user1.age)
# print(user2.email)
# print(user2.age)
#
# user1.login('user', 'pass')
# user1.login('user2', 'pass2')
