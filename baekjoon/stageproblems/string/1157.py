"""
2021.5.19
30988kb, 660ms

used 'deepcopy' and ASCII
"""
import copy
k = input()
l = [0]*26
for i in range(0,len(k)):
    q = ord(k[i])//91
    r = ord(k[i])%91
    if q == 0:
        l[(r-65)] += 1
    elif q == 1:
        l[(r-6)] += 1
l2 = copy.deepcopy(l)
l.sort()
if l[25] == l[24]:
    print("?")
else:
    print(chr(l2.index(l[25])+65))
