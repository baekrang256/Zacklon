"""
DATE - 2019/08/25
29056kb, 56ms
"""

import sys

n = (sys.stdin.readline()).split()[0]
N = 0
last = n

while True:
    N += 1
    if len(last) == 1:
        gen = last
        new = last + gen
    else:
        gen = str(int(last[0])+int(last[1]))
        if len(gen) == 1:
            new = last[1] + gen
        else:
            new = last[1] + gen[1]
    if new[0] == '0':
        new = new[1]
    s = int(new)
    r = int(n)
    if s == r:
        break
    last = new

print(N)

"""
This problem took a pretty long time even though I got the algorithm pretty early.
one of the reason it took a long time is that I was using a wrong n to compare
to be exact of what I'm saying, before this code I used n as just sys.stdin.readline()
this includes the \n for the string, so the while loop can never be break since 'last' variable can never have \n included.
so I solved it by using split, and then plucking the element out that I needed.

The second reason is, I just used the wrong algorithm
the above algorithm is correct, and it was what I intended to use at first try.
Later on, I used the algorithm below

import sys

n = (sys.stdin.readline()).split()[0]
N = 0
last = '0'

while last != n:
    N += 1
    if last == '0':
        last = n
    if len(last) == 1:
        gen = last
        new = last + gen
    else:
        gen = str(int(last[0])+int(last[1]))
        if len(gen) == 1:
            new = last[1] + gen
        else:
            new = last[1] + gen[1]
    if new[0] == '0':
        new = new[1]
    last = new

print(N)

this is almost similar. except that it was wrong when... the case is 0.
when n has 0, since last is also 0(in string. type of n is always string)
we print 0 for the case of 0, which is wrong. It should be 1.
"""
