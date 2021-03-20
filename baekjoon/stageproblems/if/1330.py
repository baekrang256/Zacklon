"""
DATE - 2019/08/24
29056kb, 56ms
"""
"""
we used readline here, but we can instead use input() to simplify the code.
"""
import sys

numbers = [int(k) for k in (sys.stdin.readline()).split()]


if numbers[0] > numbers[1]:
    print('>')
elif numbers[0] < numbers[1]:
    print('<')
else:
    print ('==')
