# Collections: Counter, namedtuple, OrderedDict, defaultdict, deque

# Counter
from collections import Counter
a = 'aaaaaaabbbbbbbbbbcccc'
my_counter = Counter(a)
# Count valaues
print(my_counter.keys())
print(my_counter.values())
print(my_counter.items())
# To get the most common value
print(my_counter.most_common(1))
print(my_counter.most_common(1)[0][0]) # Most common element
# To get a list with all the different elements
print(list(my_counter.elements()))

# namedtuple
from collections import namedtuple
print('-'*100)
Point = namedtuple('Point', 'x,y')
pt = Point(1, -4)
print(pt.x, pt.y)

# OrderDict (they just like regular dicts but remember the order that the items were inserted)
# But since python 3.7 regular dicts also remember the order
from collections import OrderedDict
print('-'*100)
# ordered_dict = OrderedDict()
ordered_dict = {}
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
print(ordered_dict)

# defaultdict (also like regular dict but they will have the default value if the key has not beem set)
from collections import defaultdict
print('-'*100)
d = defaultdict(int)
d['a'] = 1
d['b'] = 2
print(d['c'])

# deque (double ended queue)
# It can be used to add or remove elements from both ends and both are efficiently implemented
from collections import deque
print('-'*100)
d = deque()
d.append(1)
d.append(2)
d.appendleft(3)       # add element to the left 
print(d)
d.popleft()           # remove left element
d.extend([4,5,6])     # add a few elements
d.extendleft([4,5,6]) # add a few elements to the left (mirrored horizontally)
print(d)
d.rotate(1)           # all elements will be rotated 1 place
print(d)
