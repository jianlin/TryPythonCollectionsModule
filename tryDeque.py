import collections

deque1 = collections.deque([1, 2])
print(deque1)

deque1.append("hello")
deque1.appendleft(123)

print(deque1)


deque1.append("world")
deque1.appendleft(3.14)

print(deque1)

print(deque1.pop())
print(deque1)

print(deque1.popleft())
print(deque1)
