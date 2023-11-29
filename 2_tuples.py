# Create tuple from a list
tuple_from_list = tuple(['Max', 28, 'Boston'])
print(tuple_from_list)

# Access elements by index
item = tuple_from_list[0]
last_item = tuple_from_list[-1]
print(last_item)

# Count specific elements in a tuple
letter_tuple = ('a', 'p', 'p', 'l', 'e')
print(letter_tuple.count('p'))

# Get index of a specific element (returns index of first occurance of element)
print(letter_tuple.index('p'))

# Convert tuple to list and vice versa
tuple_to_list = list(letter_tuple)
list_to_tuple = tuple(tuple_to_list)
print(tuple_to_list)
print(list_to_tuple)

# Slising tuple (works just like with lists)
number_tuple = (1,2,3,4,5,6,7,8,9,10)
reverse_tuple = number_tuple[::-1]
print(reverse_tuple)

# Unpacking (must match number of elements in a tuple)
pack_tuple = ('Max', 28, 'Boston')
name, age, city = pack_tuple
print(name, age, city)

# If we want to unpack multiple values (it returns multiple elements in between as a list)
mult_tuple = (0,1,2,3,4,5)
item1, *item2, item3 = mult_tuple
print(item1, item2, item3)

# Tuple is more memory efficient since it uses 1 memory cell instead of 2 like in a list
import sys
test_list = [0, 1, 2, 'hello', True]
test_tuple = (0, 1, 2, 'hello', True)
print(sys.getsizeof(test_list), 'bytes')
print(sys.getsizeof(test_tuple), 'bytes')