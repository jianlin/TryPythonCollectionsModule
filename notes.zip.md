# zip

basically, `zip()` just takes some lists, and then give you the index 0 of each list in
a tuple, and then repeat for index 1, 2, 3, etc.

It will be the length of the shortest list... so if all others are long lists but one list has length 3, the result will only have 3 items.

it is useful for transposing a matrix, like

    [list(i) for i in zip(*m)]    # *m is like splashing it

##docs

https://docs.python.org/2/library/functions.html#zip

https://docs.python.org/3.3/library/functions.html#zip
