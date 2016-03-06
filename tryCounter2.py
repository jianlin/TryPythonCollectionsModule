import collections

arr = ['hello', 'world', 'hello', 'hi', 'hello']

counter = collections.Counter()
print counter

for i in arr:
    counter[i] += 1

print counter
