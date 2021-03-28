"""
2021.3.28
28776kb, 76ms

You know, there are lot of ways to make lists from splitting
Below used 'for'.
But you can also use the following
scores = list(map(int,input().split())
This works the same, a little shorter in code
I don't know if this is more efficient
"""

N = int(input())
scores = [k for k in map(int,input().split())]
Max = max(scores)
Total = 0
for i in range(N):
    scores[i] = (scores[i]/Max)*100
    Total += scores[i]
print(Total/N)
