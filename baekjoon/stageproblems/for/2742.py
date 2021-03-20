"""
DATE - 2019/08/24
29344kb, 112ms
"""

import sys

n = int(sys.stdin.readline())

for i in range(0,n):
    print(n-i)

"""
2021.3.20
28776kb,112ms

another way
"""
a = int(input())
for i in range(a, 0, -1):
    print(i)
