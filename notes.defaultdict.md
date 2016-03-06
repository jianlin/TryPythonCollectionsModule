# TryPythonCollectionsModule


## defaultdict

you need to pass in a factory ... a class (or a function?)...

hm... it is a "callable", and is known as a "default_factory"

Because there are 3 steps when you use d[key]

1. when d[key] is defined, all is fine
2. if not, then   d[key] = default_factory()  # to create 0, empty array, empty set, etc, by int(), list(), etc
3. now return d[key] as a reference (to object), for you to set to something or pass message to it

see, `int()` gives `0`, and `list()` gives empty array, `set()` gives empty set

### Integer or Count

    h = defaultdict(int)
    h[key] += 1

is like

    h[key] = (h[key] || 0) + 1    // JavaScript

### Array

    h = defaultdict(list)
    h[key].append(v)

is like

    h[key] ? h[key].append(val) : h[key] = [val]   // JavaScript... something like this

### Set

    h = defaultdict(set)
    h[key].add(v)

is like JavaScript's array example above... or if we use JavaScript's object's keys as a set...

    h[key] ? h[key][val] = true : h[key] = { val : true }   // JavaScript... something like this

# The ultimate point is

The ultimate point is, whatever you pass to `defaultdict`, it is what you expect the dictionary will map to.  That is, if `int`, then map to a number (a count usually).  If array, then map to array, etc. (empty array to begin with).
