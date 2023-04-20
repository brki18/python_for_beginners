list = [1, 2, 3, 4, 5]
list2 = [1, 'a', 2.54, True]

# print(list)
# print(list2)
#
# print(list2[2])

# Slicing

# print(list[0:3])
# print(list[0::2])

# Lists are mutable

# new_list = list
new_list = list[:]
new_list[2] = 13

# print(list)
# print(new_list)

# Matrix
matrix = [[[11, 12], 1, 2, 3], [4, 5, 6], [7, 8, 9]]

# print(matrix[0][0][1])

# List methods
list_methods = [1, 2, 3, 4]
# Add items to list
list_methods.append(13)
list_methods.insert(2, 22)
extend = [11, 33, 44]
# list_methods.extend([11, 33, 44])
list_methods.extend(extend)
# print(list_methods)

# Remove list items
list_remove = [1, 2, 3, 4, 5]
list_remove2 = ['name', 'password', 'email', 'name']
list_remove.pop(2)
list_remove2.remove('password')
# print(list_remove)
# print(list_remove2)
# list_remove2.clear()
# print(list_remove2)
#
# print('name' in list_remove2)

# print(list_remove2.count('name'))
# print(list_methods)
# list_methods.sort()
sorted_list = sorted(list_methods)
# print(list_methods)
# list_methods.reverse()
reversed_list = list_methods[::-1]
# print(reversed_list)
# print(list_methods)
# print(sorted_list)
# print(range(1,100))
# list_from_range = list(range(1,100))

joined_text = '|'.join(['This', 'is', 'Python', 'course'])
print(joined_text)
