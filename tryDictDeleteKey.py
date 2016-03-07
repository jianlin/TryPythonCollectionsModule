d1 = {"ha" : 123, "hi" : 3.14}

print(d1)


del d1["ha"]
print(d1)


d1 = {"ha" : 123, "hi" : 3.14}

print(d1)


d1.pop("ha")     # pop() is much more Object oriented... for, what does del d1["ha"] mean?
                 #   To say it is not the same as del 123 because d1["ha"] is 123

print(d1)
