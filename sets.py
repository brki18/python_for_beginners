set_from_list = [1, 2, 2, 2, 3]

my_set = {1, 2, 3, 4, 5}
other_set = {4, 5, 6, 7, 8}
set_is_unique = {1, 2, 3, 3, 3, 3, 4, 5, 5}

# print(my_set.difference(other_set))
# other_set.discard(5)
# print(other_set)

# my_set.difference_update(other_set)
# print(my_set)

# print(my_set.intersection(other_set))
print(my_set & other_set)  # & -> intersection
# print(my_set.isdisjoint(other_set))

# print(my_set.union(other_set))
print(my_set | other_set)  # | -> union
#
# print(my_set.issubset(other_set))
#
# print(other_set.issuperset(my_set))

# print(set_from_list)
# print(set(set_from_list))
#
# copied_set = set_is_unique.copy()
# print(copied_set)
# copied_set.clear()
# print(copied_set)
# print(my_set)
#
# print(set_is_unique)
