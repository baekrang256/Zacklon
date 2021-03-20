"""
2021.3.20
28776kb,72ms
"""

# a much simple solution using input()


x = int(input())
for i in range(1, x+1):
    a, b = map(int, input().split())
    print(a+b)
