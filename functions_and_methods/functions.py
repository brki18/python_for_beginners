# DRY -> Don't Repeat Yourself
def say_hello():
    print('Welcome to the Python course')


# for i in range(5):
#     say_hello()


# sayHello()
# sayHello()

# Arguments vs Parameters

# Parameters are defined in a function
def print_msg(msg):
    print(msg)


# Arguments are actual values we are passing to the functions
# print_msg('This is Python course')

def welcome_msg(name, emoji):
    print(f"Welcome {name} {emoji}")


# welcome_msg('Marko', ':-)')
# welcome_msg(':-)', 'Marko')
# # keyword arguments
# welcome_msg(emoji=':-)', name='Marko')


# default arguments
def welcome_msg_default(name='Bob', emoji=':-('):
    print(f"Welcome {name} {emoji}")


# welcome_msg_default(emoji=':-0')


# Return statements

def return_msg():
    return 'This is return value'


msg = return_msg()
# print(return_msg())
return_msg()
print(msg)


def outer_func():
    msg = 'Set in outer function'

    def inner():
        return msg

    return inner()


def sum_num(num1, num2):
    def inner_sum(n1, n2):
        return n1 + n2
        print('hello')

    total_sum = inner_sum(num1, num2)
    return total_sum
    print('hello from outer')


total = sum_num(10, 20)

print(total)
# print(outer_func())
