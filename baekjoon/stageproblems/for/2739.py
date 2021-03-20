"""
DATE - 2019/08/24
29056kb, 56ms
"""

"""
it is much simple to just use input() function
"""

import sys

n = int(sys.stdin.readline())

for i in range(1,10):
    print("%d * %d = %d" % (n, i, n*i))
