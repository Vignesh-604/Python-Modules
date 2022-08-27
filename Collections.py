"""Collections :- Counter, namedtuple, OrderedDict, defaultdict and deque"""
from collections import Counter                                 # Prints number of stings.

a = "qwadwqaaeqawdaewa"
count = Counter(a)

print(count)                                   # [1]
print(count.items())                           # [2]
print(count.keys())                            # [3]
print(count.values())                          # [4]
print(count.most_common(1 and 2))              # [5]                     # (n) will define the most repeated item.
print(count.most_common(1)[0])                 # [6]                     # (n)[a] : the index of the item we want.
print(count.most_common(1)[0][1])              # [7]                     # (n)[a][b] : the key or value of that item.
print(list(count.elements()))                  # [8]

from collections import namedtuple                               # Assigns value to field names.

farm = namedtuple("Pets", "Cat, Dog")                                    # namedtuple(class_name, field_names). Spaces or symbols can't be used in class_name.
quantity = farm(6, "Red")
print(quantity)                                # [9]
print(quantity.Dog, quantity.Cat)              # [10]

from collections import OrderedDict

diction = OrderedDict()                                                  # Doesn't change the order of the dictionary.
diction["b"] = 2                                                         # But in python 3.7 or above, all dictionaries are ordered dictionaries.
diction["a"] = 1
print(diction)                                 # [11]

from collections import defaultdict                             # Gives out a default value in place of an error.

diction2 = defaultdict(bool)
diction2["a"] = 1                                                        # str = nothing    int = 0      flt = 0.0      list = []
diction2["b"] = 2                                                        # dict = {}      set = set()    tuple = ()     bool = False
print(diction2["c"])                           # [12]

from collections import deque                                   # Extra list functions.

dqe = deque()

dqe.append(1)
dqe.append(2)
dqe.appendleft(9)
dqe.appendleft(8)
print(dqe)                                     # [13]

dqe.pop()                                                                 # Removes last item.
dqe.popleft()                                                             # Removes the last item (first) from left.
print(dqe)                                     # [14]

dqe.extend([3, 5, 6])
dqe.extendleft([-1, -3, -5])
print(dqe)                                     # [15]

dqe.rotate(2), print(dqe)                      # [16]                     # Shifts the list n places to the right.
dqe.rotate(-3), print(dqe)                     # [17]                     # Shifts the list n places to the left if it has - sign before n.

dqe.clear(), print(dqe)                        # [18]                     # Clears the list.
