"""
2021.5.19
28776kb, 80ms
"""

s = input()
l = ['=','-','j']
t = 0
for i in range(0,len(s)):
    if s[i] == l[0]:
        if s[i-1] == 'z':
            if s[i-2] == 'd':
                t = t - 1
            continue
        continue
    elif s[i] == l[1]:
        continue
    elif s[i] == l[2]:
        if s[i-1] == 'l' or s[i-1] == 'n':
            continue
        t=t+1
    else:
        t = t + 1
print(t)
