# TryPythonCollectionsModule


## Counter...

the other things here all need this:

    import collections


it is like a dictionary, but can be considered to have a default value of `0`

can create from array, dict, string.  need to be careful for string, because it breaks down into characters.

after the creation, you can use

    count["foo"] += 1

or

    print count["a"]

`count["foo"] += 1` will not fail as no such key, then default value is 0.

You can set it to any integer values... negative ok.
and to delete it, use

    del counter["foo"]

so that the key is gone.

## messages that can be passed to the Counter object:

### `elements()`

just like returning    `(each key) * numOccurrences`

docs say

> Elements are returned in arbitrary order

and then if count is 0 or negative, won't return anything

### `most_common(n)`

returns an array of `n` tuples, with first item in tuple as the key, and second item in tuple as the count... similar to `dict.items()`

when `n` is omitted, you can all of them, and is sorted by most common to the least common ones.

### `update(iterable or dict)`

it is important to note that update takes an iterable (or dict, and map is a more popular name than dict in python), so if you do counter.update("hello"), it will treat "hello" as an iterable and break it down in characters.  So if you want to update "hello", you need to do counter.update(["hello"]) -- the iterable, which is an array, with 1 item, which is the key "hello"

But if you just have 1 key, you may as well just do `counter["hello"] += 1`

the `update()` really is like `add()`, as you can do  `counter1.update(counter2)`
to add the items to counter1

There is `subtract()`, but there isn't an `add()`.  The `add()` is `update()`

### `subtract(iterable or dict)`

opposite of `update()`, which is to add.  The `0` and negative count will stay.
The operator `-` is also ok, and the `0` and negative will be removed in that case.
Also, if using operator `-` then it is returning new Counter object, not doing it in-place.
