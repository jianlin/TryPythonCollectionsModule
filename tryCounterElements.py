import collections

counter = collections.Counter(['hello', 'world', 'hello', 'hi', 'hello', 'hi'])

print(counter)

print(counter.most_common(1))
print(counter.most_common(2))
#print(counter.least_common(2))

print(counter["hello"])
print(counter["hi"])


print(counter.elements())

print([i for i in counter.elements()])

print(reduce(lambda a, b: a + b, [[k] * v for (k, v) in counter.items()]))