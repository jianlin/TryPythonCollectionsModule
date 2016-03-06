# TryPythonCollectionsModule


## defaultdict

you need to pass in a factory ... a class

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

    
