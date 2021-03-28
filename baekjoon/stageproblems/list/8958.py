"""
2021.3.28
28776kb, 76ms

We didn't used list(???)
Well it did used iteration.
the row variable shows how much answer we got right in a row.
we first count the number of case, then we start the 'for' loop N(number of case) times.
score starts with 0, row starts with 1, and the result of each cases will be handled by the string variable 'result'.
every time if we get the answer, we first add the score with the amount of rows of answers we got right.
And then we add the number of row.
If we got wrong, the row returns into 1.
"""

import sys
N = int(sys.stdin.readline())
for i in range(N):
    score = 0
    row = 1
    result = sys.stdin.readline()
    for i in range(len(result)):
        if result[i] == 'O':
            score += row
            row += 1
        else:
            row = 1
    print(score)

"""
2021.3.28
28776kb, 68ms
Below used list.
However the whole idea is typically same so it is meaningless.
The reason I wrote the algorithm below is to show that we can change the string into list right away using list().
"""
import sys
N = int(sys.stdin.readline())
for i in range(N):
    score = 0
    row = 1
    result = list(sys.stdin.readline())
    for i in range(len(result)):
        if result[i] == 'O':
            score += row
            row += 1
        else:
            row = 1
    print(score)
