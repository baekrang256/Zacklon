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

"""
another way to do this in much compact looking is the following
"""

n = input()
l = list(input())
s = 0
for i in l:
    s = s+i
print(s)
