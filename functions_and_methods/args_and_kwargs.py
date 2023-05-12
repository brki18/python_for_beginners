def multiple_args(*args, email='john@gmail.com', **kwargs):
    for i in args:
        print(i)
    print(args)
    print(*args)
    print(kwargs)
    for k, v in kwargs.items():
        print(k, v)
    print('args and kwargs')
    print(email)


# Order of arguments in Python functions and methods
# 1. params, 2. *args, 3. default parameters, 4. **kwargs


multiple_args(1, 2, 3, 4, 5, email='bob@live.com', name='Marko', age=36)
