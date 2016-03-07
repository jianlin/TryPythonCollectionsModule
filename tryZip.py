a = b = c = range(6)

z = zip(a,b,c)

print(z)
print(type(z))

m = [[1,2,3,4], [11,12,13,14], [101,102,103,104]]

print(m)

t = zip(m)
print("zip(m)", t)

t = zip(*m)
print("zip(*m)", t)

tm = [list(i) for i in t]
print(tm)
