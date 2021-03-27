"""
2021.3.27
28776kb, 64ms

it's a problem about list, but I used the stupid way.
well it took a similar time as the idel solution, but the code is long.
"""

import sys
n = int(sys.stdin.readline())
min = n
max = n
k = 1
for i in range(0,8):
    t = int(sys.stdin.readline())
    if t>max:
        max = t
        k = i+2 
print(max)
print(k)
        
