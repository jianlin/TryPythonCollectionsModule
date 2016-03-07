# dict

the first thing to know is that you should not use `dict` as a variable name.
Python will let you do it.  But think about what happens when you do `dict(dict)`
then.  You are re-defining the type `dict`.  If you use `dict` as a variable name, only linting will give you warning.  Python will not.

## removing a key

    del d[key]

and  

    d.pop(key)

will both work.  Although I like `d.pop(key)` a lot more, because `del d[key]` feels like
it is `del 123` if `d[key]` evaluates to `123`.
