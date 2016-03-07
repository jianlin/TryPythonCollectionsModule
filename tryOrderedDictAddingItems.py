import collections

odict = collections.OrderedDict();
print(odict)

odict["ha"] = 123;
print(odict)
print(odict["ha"])

# print(odict[0])  # when you print it out, it looks like an array of tuples, but it is not
                   #   You still use it just like a dict


odict["z"] = 3.14;
print(odict)

odict["a"] = 1.618;
print(odict)

print([(k,v) for k,v in odict.items()])
print(odict.items())
print(odict.items()[0])     # so odict.items() is really an array of tuples
print(type(odict.items()[0])) 
