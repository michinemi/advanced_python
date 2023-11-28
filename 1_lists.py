test_list = ['banana', 'cherry', 'apple']
test_list_2 = [10, 1, 5, 2, 8, 11, 9, 7, 6, 4, 3]

# Get last item in a list
# print(test_list[-1])

# Insert item in a list
# test_list.append('lemon')
# print(test_list)

# Insert an item at a specific position
# test_list.insert(0, 'blueberry')
# print(test_list)

# Remove and return element from a list
# test_item = test_list.pop()
# print(test_item)
# print(test_list)

# Remove specific element from a list
# test_list.remove('blueberry')
# print(test_list)

# Remove all elements
# test_list.clear()
# print(test_list)

# Reverse the list
# test_list.reverse()
# print(test_list)

# Sort list. NOTE: Works as inplace
# test_list.sort()
# test_list_2.sort()
# print(test_list)
# print(test_list_2)

# To create new sorted list
# new_test_list_2 = sorted(test_list_2)
# print(test_list_2)
# print(new_test_list_2)

# To create new list with the same elements
# dup_lists = [0] * 5
# print(dup_lists)

# Concat lists
# concat_list = test_list_2 + dup_lists
# print(concat_list)

# Slicing with steps
# slice_list = test_list_2[::3]
# print(slice_list)

# Another way to reverse list
# slice_list_2 = test_list_2[::-1]
# print(test_list_2)
# print(slice_list_2)

# Copying list. NOTE: modifying this copy will also modify the original list
# list_copy = test_list
# list_copy.append('lemon')
# print(list_copy)
# print(test_list)

# To make an actual copy (3 ways to do so)
# list_copy = test_list.copy()
# list_copy = list(test_list)
# list_copy = test_list[:]
# list_copy.append('lemon')
# print(list_copy)
# print(test_list)

# List comprehension. Nice way to create a new list from an existing list with 1 line of code
list_comp = [item*item for item in test_list_2]
print(list_comp)