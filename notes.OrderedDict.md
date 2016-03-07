# TryPythonCollectionsModule


## OrderedDict

I think one of the biggest take away point is that: OrderedDict is just a subclass of `dict`, and you
can use it just like it is a `dict`.

But just that internally, it is ordered.

When you print it out, it looks like an array of tuples, but it is not.  It is still just a dictionary,
and use just like that:  d["foo"]

so when you popitem(), it will be the last,
and when you popitem(last=False), it will be the first item that is popped.

Contrast with `pop()`, which is to pop a certain key, as `pop(key)`, which is the same as `del d[key]`

To iterate over the k, v pair, still use

    for k, v in odict.items()

    
