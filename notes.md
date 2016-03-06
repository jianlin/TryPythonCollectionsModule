# TryPythonCollectionsModule


## Counter...

the other things here all need this:

    import collections


like a dictionary, but can be considered to have a default value of `0`

can create from array, dict, string.  need to be careful for string, because it breaks down into characters.

after the creation, you can use

    count["foo"] += 1

or

    print count["a"]

`count["foo"] += 1` will not fail as no such key, then default value is 0.
