import collections

counter = collections.Counter(['hello', 'world', 'hello', 'hi', 'hello', 'hi'])

print(counter)

print(counter.most_common(1))
print(counter.most_common(2))
#print(counter.least_common(2))

print(counter["hello"])
print(counter["hi"])

counter = counter + collections.Counter("hello")
print(counter)


counter = collections.Counter(['hello', 'world', 'hello', 'hi', 'hello', 'hi'])
counter = counter + collections.Counter(["hello"])
print(counter)


counter = collections.Counter(n = 2, level = 3, ha = 1)

print(counter)

counter2 = collections.Counter(n = 1000, ha = 2000)
counter = counter + counter2

print(counter, counter2)


counter = counter + collections.Counter({"hmm": 1, "ha": 10000000})

print(counter)

counter = counter + collections.Counter(["ha", "hello", "ha", "level"])     # add won't work... subtract works, but add won't work

print(counter)
