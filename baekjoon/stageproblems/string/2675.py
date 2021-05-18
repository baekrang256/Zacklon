"""
2021.5.18
28776kb, 76ms
"""

import sys
n = int(input())
for i in range(0,n):
    s = ''
    a, b = map(str, sys.stdin.readline().split())
    for i in range(0,len(b)):
        s = s + b[i]*int(a)
    print(s)
