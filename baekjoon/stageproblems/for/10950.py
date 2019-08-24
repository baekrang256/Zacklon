"""
DATE - 2019/08/24
29056kb, 56ms
"""

import sys

T = int(sys.stdin.readline())

for i in range(1,T+1):
    line = [int(k) for k in (sys.stdin.readline()).split()]
    print(line[0]+line[1])
