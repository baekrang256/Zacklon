"""
DATE - 2019/08/24
29056kb, 56ms
"""

import sys

N = int(sys.stdin.readline())

for i in range(1,N+1):
    print("*"*i)
    
"""
2021.3.27
28776kb, 72ms

another way
"""

n = int(input())
s = '*'
for i in range(0,n):
    print(s)
    s += '*'
