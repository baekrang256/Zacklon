"""
2021.5.25
31312kb, 76ms

using for statement is not recommended since the range of V is really large, and there is a time limit of 0.15 seconds.
+ it doesn't really matter to use int as any range of integer.
There was long type for integer in old version python, but it no longer exists.
see the following link for more information
https://stackoverflow.com/questions/27632707/assign-and-print-long-variable-in-python
"""

import math
A, B, V = map(int, input().split())
print(math.ceil((V-A)/(A-B)+1))
