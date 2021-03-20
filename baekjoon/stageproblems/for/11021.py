"""
DATE - 2019/08/24
29056kb, 56ms
"""

import sys

T = int(sys.stdin.readline())

for i in range(1,T+1):
    num = [int(k) for k in (sys.stdin.readline()).split()]
    print("Case #%d: %d" % (i, num[0]+num[1]))
    
"""
2021.3.21
28776kb,80ms

We don't know the maximum cases for this algorithm.
using input() function absolutely takes more time compared to the above algorithm
(you can see that by having a time gap of 24ms.)
However it still worked... but remember that above algorithm is much more efficient according to time.
"""
n = int(input())
for i in range(1,n+1):
    a, b = map(int, input().split())
    print("Case #%d: %d" %(i, a+b))
    
"""
2021.3.21
28776kb, 72ms

This is another way of using readline().
This took a little bit more time compared to the first algorithm
I think it's because of a server issue that later appeared in boj, because when I applied the first algorithm today(21.3.21), it took same time with this algorithm.
"""

import sys

n = int(sys.stdin.readline())

for i in range(1,n+1):
    a, b = map(int, sys.stdin.readline().split())
    print("Case #%d: %d" %(i, a+b))
