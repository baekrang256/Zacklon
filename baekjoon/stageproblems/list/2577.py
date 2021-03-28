"""
2021.3.28
28776kb, 76ms

appended the each digit of the multiplied number using the first for statement
then used the count() method to count it.
"""
import sys
l = []
A = int(input())
B = int(input())
C = int(input())
M = str(A*B*C)
for i in range (0,len(M)):
    l.append(int(M[i]))
for i in range(0,10):
    print(l.count(i))
