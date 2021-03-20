"""
DATE - 2019/08/24
29056kb, 56ms
"""

import sys

n = int(sys.stdin.readline())
sum = 0

for i in range(1,n+1):
    sum += i

print(sum)

# a little bit simpler calculation,
# 2021.3.20, 28776kb, 64ms

x = 0
for i in range(1,int(input())+1):
    x+=i
print(x)
