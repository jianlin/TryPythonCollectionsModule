import collections

counter = collections.Counter({"isn't": 1, "it": 3, "same": 2, "as": 5, "dict": 1})

print(counter)

print(counter.most_common(1))
print(counter.most_common(2))
#print(counter.least_common(2))
