
"""
No.1003
29056KB, 56ms
"""

import sys

fibo_list = list()
for i in range(0,40):
    if i == 0 or i == 1:
        fibo_list.append(1)
    else:
        fibo_list.append(fibo_list[i-1]+fibo_list[i-2])

T = int(sys.stdin.readline())
for i in range(0,T):
    N = int(sys.stdin.readline())
    if N == 0:
        print("1 0")
    elif N == 1:
        print("0 1")
    else:
        print("%d %d" % (fibo_list[N-2], fibo_list[N-1]))
