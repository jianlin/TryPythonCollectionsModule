# list

something that is different from other languages:

`l.reverse()` doesn't return a new list.  It just reverse the list "in-place", just like Ruby's `l.reverse!()`

To get a new reversed list, use `reversed(l)`.  Note that it is not `reverse()`, it is `reversed()`

As with `dict`, cannot use `list` as a variable name.  Python will not error on you, but I think it should, because `list` is such a standard type, built-in, and so fundamental to Python.


## Tutorial and reference

https://docs.python.org/3/tutorial/introduction.html#lists

https://docs.python.org/3/tutorial/datastructures.html#more-on-lists

https://docs.python.org/3/tutorial/stdlib2.html#tools-for-working-with-lists


https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range

https://docs.python.org/3/library/stdtypes.html#lists

## converting to a list

can just use

    list(something)

instead of

    [i for i in something]

## removing an item at the front or tail

    li.pop()
    li.pop(0)     # remove in front, but use deque if need to do it often, or else slow

## adding an item at the tail or front

    li.append()          # at the end
    li.insert(0, item)   # in front, but slow.  use deque 
