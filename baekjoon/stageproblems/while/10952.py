"""
DATE - 2019/08/25
29056kb, 56ms
"""

import sys

while True:
    a = [int(k) for k in (sys.stdin.readline()).split()]
    if a[0] == 0:
        break
    else:
        print(a[0]+a[1])
