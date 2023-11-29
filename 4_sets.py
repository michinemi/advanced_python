# Sets are unordered, mutable, no duplicates
test_set = {1,2,3,4,2}
test_set2 = set('hello')
print(test_set2)

# To create an empty set
empty_set = set()

# Add and remove elements in set
empty_set.add(1)
empty_set.remove(1)
print(empty_set)

# Remove non-existing item without error
empty_set.discard(135)
print(empty_set)

# Clear set
empty_set.clear()

# Remove and return first element from a list
fruit_set = {'banana', 'cherry', 'apple'}
fruit_set.pop()
print(fruit_set)

# Union and intersection
odds = {1,3,5,7,9}
evens = {0,2,4,6,8}
primes = {2,3,5,7}
union = odds.union(evens)
intersection = odds.intersection(primes)
print(union)
print(intersection)

# Difference of two sets (they not modify the original set)
setA = {1,2,3,4,5,6,7,8,9}
setB = {1,2,3,10,11,12}
diff = setA.difference(setB)
diff2 = setB.symmetric_difference(setA)
print(diff2)

# To modify inplace
setA.update(setB)
setA.intersection_update(setB)
setA.difference_update(setB)
setA.symmetric_difference(setB)
print(setA)

# Subset, superset and disjoint methods
# issubset() - if all elements are in second set = True
# issuperset() - if all elements from second set in first set = True
# isdisjoint() - if both seta have a null intersection (no same elements) = True 
setC = {1,2,3,4,5,6}
setD = {1,2,3}
print(setC.issubset(setD))
print(setC.issuperset(setD))
print(setC.isdisjoint(setD))

# Copying works just like with lists

# Frozen set - immutable version of normal set
# Works union, intersection and difference
frozen_set = frozenset([1,2,3,4])
print(frozen_set)