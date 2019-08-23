"""
DATE - 2019/08/23
29056kb, 60ms
"""

import sys

a = sys.stdin.readline()
b = a.split()
b2 = [int(k) for k in b]
print((b2[0]+b2[1])%b2[2])
print((b2[0]%b2[2]+b2[1]%b2[2])%b2[2])
print((b2[0]*b2[1])%b2[2])
print((b2[0]%b2[2]*b2[1]%b2[2])%b2[2])
