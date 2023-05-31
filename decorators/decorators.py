# Higher Order Function

def wraper(func):
    func()


def wrapper_return(msg):
    def say_hello(msg):
        print(msg)

    return say_hello(msg)


# def hello():
#     print("Helooo")


# wraper(hello)
# wrapper_return("Say Helooo")

def my_decorator(func):
    def wrap_func(x):
        print('******')
        func(x)
        print('******')

    return wrap_func


@my_decorator
def hello(msg):
    print(msg)


hello('Hello')
# my_decorator(hello("Hello"))
