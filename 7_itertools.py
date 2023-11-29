# Itertools: product, permutations, combinations, accumulate, groupby, and infinite iterators

# product
from itertools import product
a = [1,2]
b = [3]
prod = product(a,b)
print(list(prod))
prod = product(a,b, repeat=2)
print(list(prod))

# permutations (will return all possible orderings of an input)
from itertools import permutations
c = [1,2,3]
perm = permutations(c)
perm = permutations(c, 2) # specifies the length of permutation
print(list(perm))

# combinations (will make all possible combination with a specified length)
# To have the same argumaents or repetitions (e.g. 2,2) import combinations_with_replacement
from itertools import combinations, combinations_with_replacement
d = [1,2,3,4]
comb = combinations(d, 2)
comb2 = combinations_with_replacement(d, 2)
print(list(comb2))

# accumulate (by default computes sums)
from itertools import accumulate
import operator
e = [1,2,5,3,4]
acc = accumulate(e)
acc2 = accumulate(e, func=operator.mul)
acc3 = accumulate(e, func=max)
print(e)
print(list(acc3))

# groupby (returns keys and groups from an iterable)
from itertools import groupby
print('-'*100)
def smaller_that_3(x):
    return x < 3
f = [1,2,3,4]
group_obj = groupby(f, key=smaller_that_3)
# lambda is small one-line function that can have an input and we'll do some expression and return output
# So we can write this function in one line:
# def smaller_that_3(x):
#   return x < 3
group_obj = groupby(f, key=lambda x: x<3)
for key, value in group_obj:
    print(key, list(value))
# Another example of lambda
persons = [{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 25}, 
           {'name': 'Lisa', 'age': 27}, {'name': 'Claire', 'age': 28}]
group_obj = groupby(persons, key=lambda x: x['age'])
for key, value in group_obj:
    print(key, list(value))

# infinite iterators
from itertools import count, cycle, repeat
# Makes infinite loop that starts at 10 and then adds 1 every repitition
for i in count(10):
    print(i)
    if i == 15:
        break
# cycle (it will cycle infinitely through an iterable)
g = [1,2,3]
for i in cycle(g):
    print(i)
# repeat (it will simply make infinite loop)
# 1argument: is what to repeat
# 2argument: how many times to repeat
for i in repeat(9,5):
    print(i)