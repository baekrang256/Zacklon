"""
2021.3.28
28776kb, 76ms

string also has a count method by itself.
So, we multiply each of the numbers, then use the count method to find out the number of 0~9 existing in the multiplied number.
"""

a = int(input())
b = int(input())
c = int(input())

for i in range(0, 10):
    print(str(a*b*c).count(str(i)))
