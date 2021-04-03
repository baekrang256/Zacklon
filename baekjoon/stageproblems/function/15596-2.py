"""
2021.4.3
389828kb, 380ms

since list is iterable, just using the variable name itself can be possible like below.
not using 'range()' and 'len()', we use the list itself.
However this takes much longer time(about 1 sec) compared to the first solution.
I guess the reason is because this person used +=.

"""

def solve(num_list):
    sum = 0
    for i in num_list:
        sum += i
    return sum
  
"""
2021.4.3
389828kb, 164ms

so I changed it a bit, and it works really fast
"""

def solve(a):
    sum = 0
    for i in a:
        sum = sum + i
    return sum
