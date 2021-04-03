"""
2021.4.3
389828kb, 248ms

for more about learning a simple way of making a function, visit this link.
https://wikidocs.net/24
"""

def solve(a):
    ans = 0
    for i in range(0,len(a)):
        ans = ans + a[i]
    return ans
