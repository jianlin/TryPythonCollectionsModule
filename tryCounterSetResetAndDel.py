import collections

s = """
All JavaScript objects inherit the properties and methods from their prototype. Objects created using an object literal, or with new Object(), inherit from a prototype called Object.prototype. Objects created with new Date() inherit the Date.prototype. The Object.prototype is on the top of the prototype chain.
"""

arr = s.split()

print(arr)

counter = collections.Counter(arr)

print(counter)

print(counter.most_common(1))
print(counter.most_common(2))
print(counter.most_common(3))
#print(counter.least_common(2))

counter["inherit"] = 123
print(counter.most_common(3))

counter["inherit"] = 0
print(counter.most_common(3))
print(counter.most_common(300))

counter["inherit"] = -12345
print(counter.most_common(3))
print(counter.most_common(300))

del counter["inherit"]
print(counter.most_common(3))
print(counter.most_common(300))