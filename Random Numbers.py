"""Random numbers :- Modules used : random, secrets and numpy."""
from random import*

# Basic Random functions
a = random()                                                           # Random 15 digit float number after the decimal.
print(a)                               # [1]

b = uniform(1, 10.5)                                                   # Random float number within range
print(b)                               # [2]

c = randint(1, 10)                                                     # Prints an int number within range including the stop range number.
print(c)                               # [3]

d = randrange(1, 10)                                                   # Prints an int number within range excluding the stop range number.
print(c)                               # [4]

e = normalvariate(0, 2)                                                # (mu, sigma) mu : mean     sigma : standard deviation
print(e)                               # [5]

lst = ["Apple", "Banana", "Cherry", "Dragonfruit"]

f = choice(lst)                                                        # Takes a random element from the list.
print(f)                               # [6]

g = sample(lst, 2)                                                     # Takes multiple random elements from the list. No repetition.
print(g)                               # [7]

h = choices(lst, k=3)                                                  # Takes multiple random elements from the list. Repetition.
print(h)                               # [8]

shuffle(lst)                                                           # Shuffles the elements of the list.
print(lst)                             # [9]

# Random seed

seed(1)                                                                # The random output for a given parameter is fixed in a seed.
print(uniform(1, 10))                  # [10]
print(choice(lst))                     # [11]

seed(2)                                                                # If a random function is printed under the same seed, it'll give out the same results
print(choices(lst, k=1))               # [12]                                                        given the parameters are same.
print(randint(5, 10))                  # [13]

seed(1)
print(uniform(11, 15))                 # [14]
print(choice(lst))                     # [15]

seed(2)
print(choices(lst, k=1))               # [16]

# Generating random numbers from Secrets module
import secrets

i = secrets.randbelow(10)                                              # A random int under the exclusive upper bound (given number). Excl. upper bound
print(i)                               # [17]

j = secrets.randbits(4)                                                # A random int with (k) bit binary value. For ex. 8 = 1000 : 4 bits
print(j)                               # [18]

k = secrets.choice(lst)                                                # Random element from list.
print(k)                               # [19]

# Creatng random numbered lists using Numpy module.
from numpy import *                                                    # All functions below are numpy functions and not random functions.

l = random.rand(4)                                                     #  Creates a list with 'n' float numbers.
print(l)                               # [20]

l = random.rand(2, 3)                                                  #  Creates a list with (row, column) float numbers.
print(l)                               # [21, 2]

m = random.randint(0, 10, 3)                                           # Random numbered ist within range (start, stop, size) excluding stop number.
n = random.randint(0, 10, (2, 2))                                      # The tuple denotes (row, column).
print(n, m)                            # [22, 2]

arr = array([[1, 2], [3, 4], [5, 6]])                                  # Creates an array (list) of given values in each line.
print(arr)                             # [23, 3]

random.shuffle(arr)                                                    # Shuffles the contents
print(arr)                             # [24, 3]

# Note: Numpy uses a different number generator than the random or secrets module. Thereby the seeds for random and numpy are totally different.
