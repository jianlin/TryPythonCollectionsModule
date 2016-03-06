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
#print(counter.least_common(2))

