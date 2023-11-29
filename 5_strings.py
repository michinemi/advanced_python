# Strings are ordered and immutable

# To remove whitespaces
whitespace_str = '     Hell     '
whitespace_str = whitespace_str.strip()
print(whitespace_str)

# To check if string starts or ends with a specific character if substring
print(whitespace_str.startswith('H'))
print(whitespace_str.endswith('l'))

# Find an index of a character or substring
print(whitespace_str.find('e'))
print(whitespace_str.find('e'))

# Count the number of characters or substring
print(whitespace_str.count('ll'))

# Replace characters or substring (it doesn't modify the original string)
print(whitespace_str.replace('Hell', 'Heaven'))

# Convert string to list (default delimeter is ' ')
str_to_list = 'lord, have mercy'
list_from_str = str_to_list.split()
print(list_from_str)

# Convert list to string (good way to do so)
new_string = ' '.join(list_from_str)
print(new_string)

# String formatting
# %s: for strings
# %d: for integer
# %f: for float
test_var = 'joke'
test_string2 = 'This %s is very funny' % test_var
test_string3 = 'This {} is very funny'.format(test_var)
test_string = f'This {test_var} is very funny'
print(test_string3)