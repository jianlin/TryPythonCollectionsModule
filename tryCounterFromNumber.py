import collections

counter = collections.Counter(12312345)   # will error:  not iterable

print(counter)

print(counter.most_common(1))
print(counter.most_common(2))
