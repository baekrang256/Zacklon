"""
DATE - 2019/08/23
29056kb, 56ms
"""

import sys

n1 = int(sys.stdin.readline())
n2 = sys.stdin.readline()
sum = 0

for i in range(0,3):
    arb = n1*int(n2[2-i])
    sum += arb*(10**i)
    print(arb)

print(sum)
