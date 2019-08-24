"""
DATE - 2019/08/24
29196kb, 56ms
"""

import sys

nums = [int(k) for k in (sys.stdin.readline()).split()]
A = [int(k) for k in (sys.stdin.readline()).split()]

N = nums[0]
X = nums[1]
string = ''

for i in range(0,N):
    if A[i]<X:
        string += '%d ' % A[i]

print(string.rstrip())

"""
for more information about rstrip, visit the following link
https://docs.python.org/3/library/stdtypes.html?highlight=rstrip#text-sequence-type-str
"""
