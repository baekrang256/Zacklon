"""
DATE - 2019/08/24
29056kb, 56ms
"""

import sys

width = int(sys.stdin.readline())

for i in range(1, width+1):
    star = "*"*i
    print(star.rjust(width))


#for information about rjust(), visit https://docs.python.org/3/library/stdtypes.html?highlight=rjust#str.rjust

"""
2021.3.27
28776kb, 68ms

another way, not using rjust.
"""

n = int(input())
for i in range(1,n+1):
    print(' '*(n-i)+'*'*i)
