import collections

counter = collections.Counter("hello world")

print(counter)

print(counter.most_common(1))
print(counter.most_common(2))


print(counter["l"])
print(counter["d"])
