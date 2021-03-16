"""
DATE - 2019 - 08 - 22
28776kb, 76ms
"""

import sys #importing sys to use readline()

a = sys.stdin.readline()
b = a.split() #splitting the input into list in terms of blank.
print(int(b[0])+int(b[1]))
