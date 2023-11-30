# lambda is a small one-line anonynous function
# lambda arguments: expression
add10 = lambda x: x+10
print(add10(4))

# lambda with multiple arguments
mult = lambda x,y: x*y
print(mult(2,7))

# lambda with sorted method (by default sorted by first argument)
points2D = [(1,2), (15,1), (5,-1), (10,4)]
points2D_sorted = sorted(points2D)
points2D_sorted_2 = sorted(points2D, key=lambda x: x[1]) # sorted by second argument
points2D_sorted_3 = sorted(points2D, key=lambda x: x[0] + x[1]) # sorted by sum of argument
print(points2D)
print(points2D_sorted)
print(points2D_sorted_2)
print(points2D_sorted_3)

# lambda with a map function
# map(function, sequence)
a = [1,2,3,4,5]
b = map(lambda x: x*2, a)
b2 = [x*2 for x in a] # does the same thing but using a list comprehension
print(list(b))
print(b2)

# lambda with a filter function 
# filter(function (must return True or False), sequence) 
# (will return all elements for which the function evaluates to True)
c = [1,2,3,4,5,6]
d = filter(lambda x: x%2==0, c)
d2 = [x for x in c if x%2==0] # does the same thing but using a list comprehension
print(list(d))
print(d2)

# lambda with reduce function
# reduce(function, sequence)
# (will repeatedly applies the function to the elements and returns a single value)
from functools import reduce
e = [1,2,3,4]
product_e = reduce(lambda x,y: x*y, e)
print(product_e)