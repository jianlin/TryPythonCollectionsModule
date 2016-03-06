import collections

counter = collections.Counter(['hello', 'world', 'hello', 'hi', 'hello', 'hi'])

print(counter)

print(counter.most_common(1))
print(counter.most_common(2))
#print(counter.least_common(2))

print(counter["hello"])
print(counter["hi"])

counter.update("hello")
print(counter)


counter = collections.Counter(['hello', 'world', 'hello', 'hi', 'hello', 'hi'])
counter.update(["hello"])
print(counter)


counter = collections.Counter(n = 2, level = 3, ha = 1)

print(counter)

counter2 = collections.Counter(n = 1000, ha = 2000)
counter.update(counter2)

print(counter, counter2)


counter.update({"hmm": 1, "ha": 10000000})

print(counter)

counter.update(["ha", "hello", "ha", "level"])     # add won't work... subtract works, but add won't work

print(counter)

print(counter.most_common())
n = 1; print(counter.most_common()[:-n-1:-1])    # least common
n = 2; print(counter.most_common()[:-n-1:-1])    # least 2 common
n = 3; print(counter.most_common()[:-n-1:-1])    # least 3 common


def ha(self):
    print "haha, i am ", self

collections.Counter.ha = ha

counter.ha()

def least_common(self, n=None):
    return (counter.most_common()[:-n-1:-1] if n != None else counter.most_common()[::-1])

collections.Counter.least_common = least_common

print(counter.least_common(1))
print(counter.least_common(2))
print(counter.least_common())
