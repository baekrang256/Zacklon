"""
2021.3.27
147100kb, 428ms

you know, list actually has a method that finds the min, maximum integer in data.
also, I didn't know that you can just use the method list() to make the map into list.
This is much faster actually(...)
"""

n = int(input())

data = list(map(int, input().split()))

print(min(data), max(data))
