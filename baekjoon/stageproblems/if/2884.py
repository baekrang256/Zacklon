"""
DATE - 2019/08/24
29056kb, 60ms
"""

import sys

Time = [int(k) for k in (sys.stdin.readline()).split()]

if Time[1] < 45:
    Time[1] = Time[1]+60-45
    if Time[0] == 0: Time[0] = 23
    else: Time[0] += -1
else:
    Time[1] += -45

print("%d %d" % (Time[0], Time[1]))

"""
another solution
2021.3.20
28776kb, 72ms
"""

h, m = map(int, input().split())
if m<45:
    h-=1
    if h == -1:
        h = 23
    m+=15
else:
    m-=45
hh, mm = str(h), str(m)
print(hh+" "+mm)

"""
The first code is abstract because of the use of formatting.
For more about formatting, see the link below:
https://wikidocs.net/13#_15
the below code is abstract for not importing sys and not using readline()
it can be handled easily by mapping and input() splitting
"""
