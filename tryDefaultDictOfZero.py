import collections

arr = ['hello', 'world', 'hello', 'hi', 'hello', 'hi']
dict1 = collections.defaultdict(0)   # this will error with  TypeError: first argument must be callable

for s in arr:
    dict1[s] += 1

print dict1
print dict(dict1)
