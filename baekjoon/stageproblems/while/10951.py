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

In python, if you use readline() when there is no line(readline() returns the line that hasn't been readed), it returns ''
It is notified in this link :  https://wikidocs.net/26
Also in python, if you use read() after reading the whole file(read() method reads the whole line in file), it returns ''
This is notified in this link : https://docs.python.org/3/tutorial/inputoutput.html

there is also a function called readlines()
it returns the whole file into a single list, each element of the list distinguished by '\n'.
"""

"""
2021/3/27
28776kb,68ms

this used 'not'.
for more about not, look at this link
https://dojang.io/mod/page/view.php?id=2192
if not line is True, then the algorithm breaks the while loop.
So, the question is, when does 'line' becomes False so that 'not line' becomes True?
The answer is, when it is an empty string.
Note that string is NOT empty when there is a blank. An empty string is a string with no character, even the blank doesn't exist.
An empty string is falsy in python, which means that python consider empty string to be False in boolean.
So we can use it to check if we're at the EOF.
"""

import sys

while True:
    line = sys.stdin.readline()
    if not line:
        break
    a, b = map(int, line.split())
    print(a+b)
    

