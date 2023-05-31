# print('Message'
# print(name)
# print(10 / 0)
list = [1, 2, 3, 4]

# print(list[10])

# print(10 / '2')
while True:
    try:
        age = input('What is your age: \n')
        print(10 / int(age))
    except ValueError as err:
        print('You need to enter number')
        print(f'Error {err}')
        raise FileExistsError
    except ZeroDivisionError:
        print('You cannot divide with 0')
    else:
        print('Thank you')
        break
    finally:
        print('This is always executed')
