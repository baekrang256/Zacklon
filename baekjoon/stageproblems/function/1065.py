"""
2021.5.18
28776kb, 72ms
"""

def Han_count(n):
    if n < 100:
        return n
    count = 99
    for i in range(100, n + 1):
        k = list(map(int, str(i)))
        s = k[1] - k[0]
        for j in range(1, len(k) - 1):
            if k[j + 1] - k[j] != s:
                s = 10
                break
        if s != 10:
            count = count + 1
    return count

n = int(input())
print(Han_count(n))

"""
I saw some solutions that used the condition of the problem to make the code simpler
I just did the generalized version.
