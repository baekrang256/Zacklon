"""
2021.5.25
29200kb, 80ms
"""

n = int(input())
t = 1
k = 1
while n < t:
    t = t+k
    k = k+1
n = t - n
print(f'{k-n}/{1+n}')
