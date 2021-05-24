"""
2021.5.24
31312kb, 80ms

we used int to change float into integer.
we used math functions, ceiling function to be exact, to find the least integer that is greater than t
the first if statement finds out if we can possibly make revenue.
"""

import math

l = list(map(int, input().split()))
if l[1]>=l[2]:
    print(-1)
else:
    t = l[0]/(l[2]-l[1])
    if t%1 == 0:
        print(int(t+1))
    else:
        print(int(math.ceil(t)))
