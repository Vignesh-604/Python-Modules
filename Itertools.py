"""Itertools :- product, permutations, combinations, accumulate, groupby and infinite iterators."""
from itertools import product

a = [7, 8]
b = [2, 3]
c = [6]
pro = product(a, b)                                                # Will pair elements with each other.
pro2 = product(a, c, repeat=2)                                     # Will repeat the pairing.
print(list(pro))                            # [1]
print(list(pro2))                           # [2]

from itertools import permutations

d = [1, 2, 3]
perm = permutations(d)                                            # Shuffles the elements to get different combinations.
perm2 = permutations(d, 2)                                        # (seq,n) seq = list_name   n = no. of elements in one tuple.
print(list(perm))                           # [3]
print(list(perm2))                          # [4]

from itertools import combinations, combinations_with_replacement

e = [1, 2, 3, 4]                                                  # Similar to permutations, but does not have same values in different arrangement.
comb = combinations(e, 2)                                         # For ex. If (2, 3) is printed, (3, 2) won't be printed.
print(list(comb))                           # [5]                 # Nor will the values repeat. For ex. (1, 1).

comb2 = combinations_with_replacement(e, 2)                       # The same values will be repeated.
print(list(comb2))                          # [6]

from itertools import accumulate
import operator

f = [1, 2, 3, 4, 5]

acc = accumulate(f)                                               # Adds upto the next value.
print(list(acc))                            # [7]

acc2 = accumulate(f, operator.mul)                                # Other operator functions include sub, div, add, etc
print(list(acc2))                           # [8]

g = [1, 4, 2, 5, 7, 2, 29, 16]
acc3 = accumulate(g, max)                                         # If the next number is smaller, then it'll print itself.
print(list(acc3))                           # [9]                 # Similar for Min.

from itertools import groupby

g = [1, 2, 3, 4, 5, 6]

def smol(x):                                                      # The function defines the argument.
    return x < 4

grp = groupby(g, key=smol)                                        # groupby(seq, key= arg).
                                                                  # It'll put the contents of list in the function.
for k, v in grp:
    print(k, list(v))                       # [10, 2]

grp2 = groupby(g, lambda x: x < 4)                                # Works same with lambda functions as well.
                                                                  # It'll put the contents of list in the lambda func.
for k, v in grp2:
    print(k, list(v))                       # [11, 2]

farm = [{"animal": "Buffalo", "quantity": 16}, {"animal": "Cow", "quantity": 12},
        {"animal": "Goats", "quantity": 6}, {"animal": "Sheep", "quantity": 6},
        {"animal": "Cats", "quantity": 9}, {"animal": "Dogs", "quantity": 12, }]

farm2 = groupby(farm, lambda i: i["quantity"])                    # It'll group together those with same values.
for o, p in farm2:                                                # It'll only group if they are next to each other.
    print(o, list(p))                        # [12, 4]

from itertools import count, repeat, cycle

for p in count(1):                                                # It'll count until a break value is given.
    print(p)                                 # [13, 3]
    if p == 3:
        break

for q in repeat(5, 3):                                            # repeat(value, n). It'll repeat the value n times.
    print(q)                                 # [14, 3]

#k = [1, 2]
#for i in cycle(k):                                               # It'll loop through the list infinitely unless a stop condition is provided.
#    print(k)                                # [15]
