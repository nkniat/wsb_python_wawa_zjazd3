>>> a = {1, 2, 3, 4}
>>> b = {2, 3, 4, 5}
>>> c = {3, 4, 5, 6}
>>> d = {4, 5, 6, 7}

>>> a.union(b, c, d)
{1, 2, 3, 4, 5, 6, 7}

>>> a | b | c | d
{1, 2, 3, 4, 5, 6, 7}

>>> a.intersection(b, c, d)
{4}

>>> a & b & c & d
{4}

>>> a.difference(b, c)
{1, 2, 3}

>>> a - b - c
{1, 2, 3}

>>> a = {1, 2, 3, 4, 5}
>>> b = {10, 2, 3, 4, 50}
>>> c = {1, 50, 100}

>>> a ^ b ^ c
{100, 5, 10}

#Curiously, although the ^ operator allows multiple sets, the .symmetric_difference() method doesn’t:
>>> a.symmetric_difference(b, c)
# Traceback (most recent call last):
#   File "<pyshell#11>", line 1, in <module>
#     a.symmetric_difference(b, c)
# TypeError: symmetric_difference() takes exactly one argument (2 given)