"""
2021.3.20
28776kb,64ms
"""
"""
can't use input(), or mapping since input is entered in two lines.
"""

import sys

x = int(sys.stdin.readline())
y = int(sys.stdin.readline())

if x>0:
    if y>0:
        print('1')
    else: print('4')
else:
    if y>0:
        print('2')
    else: print('3')
