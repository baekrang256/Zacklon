"""
DATE - 2019/08/24
29056kb, 56ms
"""

import sys

T = int(sys.stdin.readline())

for i in range(1,T+1):
    num = [int(k) for k in (sys.stdin.readline()).split()]
    print("Case #%d: %d + %d = %d" % (i, num[0], num[1], num[0]+num[1]))

"""
2021.3.21
28776kb,68ms

used map
"""

import sys

T = int(sys.stdin.readline())

for i in range(1,T+1):
    num = [int(k) for k in (sys.stdin.readline()).split()]
    print("Case #%d: %d" % (i, num[0]+num[1]))
    
"""
2021.3.21
28776kb, 80ms

used input() and map()
as expected, it takes a bit more time
"""

n = int(input())
for i in range(1,n+1):
    a, b = map(int, input().split())
    print("Case #%d: %d + %d = %d" % (i,a,b,a+b))
