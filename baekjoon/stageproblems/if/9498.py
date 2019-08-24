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
