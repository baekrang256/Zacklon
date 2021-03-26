"""
DATE - 2021/3/27
28776kb,68ms
"""

import sys
while True:
    l = [int(k) for k in sys.stdin.readline().split()]
    if l == [0,0]:
        break
    print(l[0]+l[1])
