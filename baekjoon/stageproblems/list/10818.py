"""
2021.3.27
147116kb, 672ms

it doens't really matter to use input(), actually, since realine()/input() is only called two times per case.
It took a long time for large n when splitting... but almost all of the codes were like that.
"""


import sys
n = int(sys.stdin.readline())
lofn = [int(k) for k in sys.stdin.readline().split()]
min = lofn[0]
max = lofn[0]
for i in range(0,n):
    if min > lofn[i]:
        min = lofn[i]
    elif max < lofn[i]:
        max = lofn[i]
print('%d %d' %(min, max))
