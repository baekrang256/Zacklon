"""
2021.5.25
29200kb, 76ms

the elemnets for each level is 1, 6, 12, 18, ...
Since we can step to the another level right away in just one step
I used this algorithm to find out how much step is needed for the destination.
"""

n = int(input())
l = 1
k = 1
i = 6
while n > k:
    k = k + i
    i = i + 6
    l = l + 1
print(l)
