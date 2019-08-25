"""
DATE - 2019/08/25
29056kb, 56ms
"""

import sys

while True:
    str = sys.stdin.readline()
    if str == '':
        break
    num = [int(k) for k in str.split()]
    print(num[0]+num[1])
    
"""
This problem is similar to #10952, except that it uses EOF for termination.
It is important to know EOF for the language your learning since it is a important terminology about processing files.

If you use read(), and if there exists EOF, then nothing happens.
If EOF doesn't exist, read() will give exception.

reading in chunks make read() return empty string instead of None
I used readline to read the file in chunks(in exact, lines)

one more thing to mention is that readline, readlines, and read is all different
read reads the whole file into one string data
readline read each next line(compared to the iterator) with \n
readlines() makes the whole file into list with \n
"""
