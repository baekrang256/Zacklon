"""
2021.5.19
28776kb, 76ms
"""

l = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
a = list(input())
t = 0
for i in range(0,len(a)):
    for j in range(0,8):
        if l[j].find(a[i]) != -1:
            t = t + j + 3
            continue
print(t)
