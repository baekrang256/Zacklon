"""
2021.5.19
28776kb, 76ms

you can reverse the whole string using the below method
[a:b:-1] (a>b) will return the string starting position with b, ending position with a with being reversed.
"""

a, b = map(int, (input()[::-1]).split())
if a > b:
    print(a)
else:
    print(b)
