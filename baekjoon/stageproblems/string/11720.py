"""
2021.5.18
28776kb, 64ms
"""

n = int(input())
line = input()
s = 0
l = list(map(int,line))
for i in l:
    s = s+i
print(s)
