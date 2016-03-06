import collections

counter = collections.Counter(['hello', 'world', 'hello', 'hi', 'hello', 'hi'])

print(counter)

print(counter.most_common(1))
print(counter.most_common(2))
#print(counter.least_common(2))
