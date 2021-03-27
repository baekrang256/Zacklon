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

"""
2021.3.27
147100kb, 720ms

you can also use sorting.
but it took a pretty long time.
The reason is, it's not just about searching, it's also about moving the elements.
So it's even more inefficient than the first solution that I thought.
"""
N = int(input())
lst = list(map(int, input().split()))
lst.sort()

print(lst[0], lst[N-1])
