import collections

arr = ['hello', 'world', 'hello', 'hi', 'hello', 'hi']
dict = collections.defaultdict(int)

for s in arr:
    dict[s] += 1

print(dict)
print(dict(dict))
