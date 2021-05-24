"""
2021.5.24
29200kb, 80ms

we search the whole string one by one, but not actually one by one
if there is any case where the string appears seperately, then the whole loop breaks right away.
line 17 is above the below executions because if it doesn't, there could be an error because of a size of array.
"""

import sys

n = int(input())
k = 0
for i in range(0,n):
    s = sys.stdin.readline()
    for j in range (0,len(s)):
        if j == len(s)-1:
            k = k + 1
            break
        t = s.find(s[j],j+1)
        if t != -1:
            if t-j != 1:
                break
print(k)
