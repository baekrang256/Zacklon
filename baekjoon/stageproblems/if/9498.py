"""
DATE - 2019/08/24
29056kb, 56ms
"""

import sys

scr = int(sys.stdin.readline())

if 90<=scr<=100: print('A')
elif 80<=scr<90: print('B')
elif 70<=scr<80: print('C')
elif 60<=scr<70: print('D')
else: print('F')

"""
more simplified code below
2021.3.20
28776kb, 84ms
"""

a = int(input())
if a>= 90: print("A")
elif a>=80: print("B")
elif a>=70: print("C")
elif a>=60: print("D")
else: print("F")
