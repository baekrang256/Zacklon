"""
DATE: 2021.3.20
28776kb, 64ms
"""

"""
I tried using \n, but since print can only have one value I wasn't able to use
print(a+b "\n" a-b "\n" ...)
also, you can't use \n without having it is as a string
which means you can only use \n when it is inside "".
so you can't do the below one
print(a+b \n a-b \n ...)
"""

a, b = map(int, input().split())
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
