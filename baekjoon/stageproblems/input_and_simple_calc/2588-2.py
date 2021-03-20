"""
DATE : 2021.3.20
28776kb, 64ms
"""

"""
We can't use map() function to easily solve this problem like the problems before this in input_and_simple_calc
the reason is, the input is given in two lines, not one
if we try to use input().split(), it would only accept one input, so it can not be splitted.
Same with input().split("\n") since we only accept one input.
so we have to use readline() function.
"""

import sys

a = int(sys.stdin.readline())
b = sys.stdin.readline()
print(a*int(b[2]))
print(a*int(b[1]))
print(a*int(b[0]))
print(a*int(b))
