"""
DATE - 2019/08/24
29056kb, 56ms
"""

import sys

T = int(sys.stdin.readline())

for i in range(1,T+1):
    num = [int(k) for k in (sys.stdin.readline()).split()]
    print("Case #%d: %d + %d = %d" % (i, num[0], num[1], num[0]+num[1]))
