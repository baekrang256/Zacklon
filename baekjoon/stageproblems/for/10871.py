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

"""
2021.3.27
29284kb, 72ms

the thing is, because of baekjoon's scoring method, you don't really need to use rstrip().
It'll give you answer even wtihout rstrip().
Also, using map will make the list simpler.
"""

import sys

n, k = map(int, input().split())
l = sys.stdin.readline().split()
ans = ''
for i in range(0,n):
    if int(l[i]) < k:
        ans += '%s ' %l[i]
print(ans)
