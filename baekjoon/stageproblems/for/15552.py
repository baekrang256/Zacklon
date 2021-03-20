"""
DATE - 2019/08/24
29340kb, 1652ms
NOTE: This problem suggests ways to shorten the runtime of program while using 'for'
it is a useful information, so try visiting the link below
https://www.acmicpc.net/problem/15552
https://www.acmicpc.net/board/view/22716
"""

import sys

T = int(sys.stdin.readline())

for i in range(1, T+1):
    num = [int(k) for k in (sys.stdin.readline()).split()]
    print(num[0]+num[1])

"""
2021.3.20
28776kb, 1464ms
A little bit simpler solution.
We were able to use input() for this function, surprisingly.
however, it should be only used for the first line, not in the 'for' paragraph.
The reason is, that would really make the algorithm go long.
"""

import sys

a = int(input())
for i in range(a):
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)
