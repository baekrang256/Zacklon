"""
2021.5.19
30732kb, 108ms

This is the other solution from other programmer.
First, the programmer uppercased the whole string, then counted each of them using for.
then it obtained its max value in the list.
Then, found the index of it, and then removed it.
After removing that max, if there is another one that has the same value as max, it returns '?'
else, it returns the ASCII character.

The keypoint is that it doesn't need to deepcopy the list, resultingto faster speed.
"""

a=input()
b=a.upper()
c=[0]*26

for i in range(65,91):
    if chr(i) in b:
        c[i-65]=b.count(chr(i))
N=max(c)
d=c.index(max(c))
c.remove(max(c))

if max(c) == N:
    print('?')
else:
    print(chr(d+65))
