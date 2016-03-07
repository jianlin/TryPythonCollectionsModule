# zip

basically, `zip()` just takes some lists, and then give you the index 0 item of each list in
a tuple, and then repeat for index 1, 2, 3, etc.

It will be the length of the shortest list... so if all others are long lists but one list has length 3, the result will only have 3 items.

it is useful for transposing a matrix, like

    [list(i) for i in zip(*m)]    # *m is like splashing it

Another use for zip is to "zip together" 2 rows of items... such as

    id   name  phoneNumber
    1    mike    650-123-4567

you can use

    dict(zip(line1.split(), line2.split()))

which is the same as

    dict(zip(arrHeadings, arrData))

like zipping "id" with 1, and "name" with "mike"

## docs

https://docs.python.org/2/library/functions.html#zip

https://docs.python.org/3.3/library/functions.html#zip


## transpose a matrix on StackOverflow

http://stackoverflow.com/questions/17037566/transpose-a-matrix-in-python


You can use zip with * to get transpose of a matrix:

    >>> A = [[ 1, 2, 3],[ 4, 5, 6]]
    >>> zip(*A)
    [(1, 4), (2, 5), (3, 6)]
    >>> lis  = [[1,2,3],
    ... [4,5,6],
    ... [7,8,9]]
    >>> zip(*lis)
    [(1, 4, 7), (2, 5, 8), (3, 6, 9)]

If you want the returned list to be a list of lists:

    >>> [list(x) for x in zip(*lis)]
    [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    #or
    >>> map(list, zip(*lis))
    [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
