"""
2021.3.28
28776kb, 76ms

Idea? Simple. We add up all the scores, get the average, counts the number of people above the average, and print out the percentage.
However I had a hard time using formatting.
The question asked to print up to the 3rd decimal number of each percentage.
we need to use the format function to do that.
https://wikidocs.net/13#format
Above is the abstract description of a way to use the format function.
https://brownbears.tistory.com/421
Above shows the recommendation of the formatting that we should use for python version above 3.6.
Which is a f-string formatting.

The brief explanation of the f-string formatting exists in the first link.
https://docs.python.org/3/reference/lexical_analysis.html#f-strings
Above link shows the complicated explanation about f-string formatting.

f-string formatting's full name is actually formatted string literals.
It is useful since it is straightforward like the following example in the link below.
https://realpython.com/python-f-strings/
It is also much faster compared to the other string formatting algorithm.
Also, it allows you to use operations like printing 'a+b', while other formatting is hard or impossible to do that.
"""
import sys
N = int(sys.stdin.readline())
for i in range(N):
    l = sys.stdin.readline().split()
    k = int(l[0])
    total = 0
    per = 0
    for j in range(k):
        total += int(l[j+1])
    for j in range(k):
        if int(l[j+1]) > total/k:
            per += 1
    s = per*100/k
    print(f'{s:0.3f}%')
