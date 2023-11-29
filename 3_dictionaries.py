dict_1 = {'name': 'Max', 'age': 28, 'City': 'New York'}
dict_2 = dict(name='Mary', age=27, city='Boston')
print(dict_1)
print(dict_2)

# Access the values
value = dict_1['age']
print(value)

# Insert values
dict_1['email'] = 'max@xyz.com'
print(dict_1)

# 3 ways to delete items (popitem() removes the last inserted item)
del dict_1['name']
dict_1.pop('age')
dict_1.popitem()
print(dict_1)

# 2 ways to check if a key is inside of a dict
if 'name' in dict_2:
    print(dict_2['name'])
try:
    print(dict_2['lastname'])
except:
    print('Error')

# 2 ways to loop through the dict keys
for key in dict_2:
    print(key)
for key in dict_2.keys():
    print(key)

# Loop through the dict values
for value in dict_2.values():
    print(value)

# Loop through the dict keys and values
for key, value in dict_2.items():
    print(key, value)

# Copy dict. NOTE: modifying this copy will also modify the original dict
copy_dict = dict_2

# 2 ways to make actual copy
copy_dict2 = dict_2.copy()
copy_dict2 = dict(dict_2)

# To merge 2 dicts (all existing keys will be overwritten, but new ones will be added)
first_dict = {'firstname': 'Kyle', 'lastname': 'Nilson', 'age': 25}
second_dict = {'firstname': 'Mary', 'lastname': 'Livyns', 'age': 20, 'city': 'Boston'}
first_dict.update(second_dict)
print(first_dict)

# Use of tuples as a key (impossible to use list as a key)
tuple_key = (8,7)
dict_with_tuple = {tuple_key: 15}
print(dict_with_tuple)