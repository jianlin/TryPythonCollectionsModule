# dict

the first thing to know is that you should not use `dict` as a variable name.
Python will let you do it.  But think about what happens when you do `dict(dict)`
then.  You are re-defining the type `dict`.  If you use `dict` as a variable name, only linting will give you warning.  Python will not.

## iterate over dictionary

if you use `for` to iterate over a dictionary, then it will be for keys only:

    for i in d1:
        print i         # key only

To iterate over k, v, then use

    for k, v in d1.items()
        print k, v



## Tutorial and reference:

### Python 2:

https://docs.python.org/2/tutorial/datastructures.html#dictionaries

https://docs.python.org/2/library/stdtypes.html#mapping-types-dict

### Python 3:

https://docs.python.org/3/tutorial/datastructures.html#dictionaries

https://docs.python.org/3/library/stdtypes.html#mapping-types-dict

## removing a key

    del d[key]

and  

    d.pop(key)

will both work.  Although I like `d.pop(key)` a lot more, because `del d[key]` feels like
it is `del 123` if `d[key]` evaluates to `123`.

## iterate over k, v pair

    for k, v in d.items()

or

    for k, v in d.iteritems()
