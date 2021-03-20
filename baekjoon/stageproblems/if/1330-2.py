"""
2021.3.20
28776kb,76ms
"""
"""
using map function is much easier.
for more about map function and iterable object, find the file 1000-2.py
"""

a, b = map(int,input().split())
if a<b:
    print("<")
elif a>b:
    print(">")
else:
    print("==")
