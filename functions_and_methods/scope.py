# What variables you can access and where

total = 10


def sum_numbers(num1, num2):
    global total  # access global variable
    local_var = 4  # accessible only inside function
    total = num1 + num2
    return total


print(sum_numbers(10, 20))
print(total)


def parent_scope():
    parent_var = 'text'

    def inner_scope():
        nonlocal parent_var
        parent_var = 'inner text'
        print(parent_var)

    inner_scope()
    print(parent_var)
    return inner_scope()


parent_scope()
