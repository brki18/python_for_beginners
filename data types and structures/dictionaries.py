user = {
    'user': 'Marko',
    'age': 35,
    'programming_languages': ['java', 'python', 'golang'],
    'email': 'brki@gmail.com',
    'is_admin': True,
    1: 'number',
    'password': 123,
    'programming_languages': ['PHP', 'golang'],
    True: True,
    # not valid for key[1, 2, 3]: 'list'
}

# print(user)
# print(user['user'])
# print(user['programming_languages'][1])
list_of_maps = [{'k1': 1, 'k2': 2}, {'k3': 3, 'k4': 4}]

# print(list_of_maps[1]['k3'])

# print(user['password'])
# print(user.get('password'))
# print(user.get('password', 'secret'))

# print(user.keys())
# print(user.values())
# print(user.items())
# user.clear()
# print(user)
new_dict = user.copy()
# user.clear()
# print(user)
new_dict.pop('age')
# new_dict.popitem()
new_dict.update({'email': 'brki@live.com'})
print(new_dict)
print(user)
