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
