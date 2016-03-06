import collections
from functools import reduce    # needed for Python 3

counter = collections.Counter(['hello', 'world', 'hello', 'hi', 'hello', 'hi'])

print([i for i in counter.elements()])

print(reduce(lambda a, b: a + b, [[k] * v for (k, v) in counter.items()]))