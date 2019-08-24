"""
DATE - 2019/08/24
29056kb, 56ms
"""

import sys

n = [int(d) for d in (sys.stdin.readline()).split()]

if n[0] <= n[1]:
    if n[0] >= n[2]: print(n[0])
    elif n[1] >= n[2]: print(n[2])
    else: print(n[1])
else:
    if n[0] <= n[2]: print(n[0])
    elif n[1] <= n[2]: print(n[2])
    else: print(n[1])
