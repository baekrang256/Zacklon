"""
DATE - 2019-08-24
29056kb, 60ms
"""

"""
you can use input() to simplify the code
"""

import sys

year = int(sys.stdin.readline())

if (year%4 == 0 and year%100 != 0) or year%400 == 0: print(1)
else: print(0)
