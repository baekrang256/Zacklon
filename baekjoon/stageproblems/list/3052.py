"""
2021.3.28
28776kb,76ms

The solution works as following
1) We add the first number's remainder divided by 42.
2) Starting from the second number, if the remainder divided by 42 of the number already exists in the list, we don't add it in the list
if it doesn't exists, we add append it into the list.
3) The list only has non-duplicate remainders of all 10 numbers, so the length of the list is same as the number of different remainders for 10 numbers.

We used 'in' to see if the specific remainder already exists in the list.
https://dreamjy.tistory.com/93
"""

import sys
l = []
for i in range(10):
    if i == 0:
        l.append(int(sys.stdin.readline())%42)
    else:
        k = int(sys.stdin.readline())%42
        if k in l:
            continue
        else:
            l.append(k)
print(len(l))
