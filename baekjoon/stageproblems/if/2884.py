"""
DATE - 2019/08/24
29056kb, 60ms
"""

import sys

Time = [int(k) for k in (sys.stdin.readline()).split()]

if Time[1] < 45:
    Time[1] = Time[1]+60-45
    if Time[0] == 0: Time[0] = 23
    else: Time[0] += -1
else:
    Time[1] += -45

print("%d %d" % (Time[0], Time[1]))
