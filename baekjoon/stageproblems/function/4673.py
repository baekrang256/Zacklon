"""
2021.5.18
4940ms, 29028kb
"""

def d(n):
    d = list(map(int,str(n)))
    k = n
    for i in d:
        k = k+i
    return k
l = []
for i in range(1,10001):
    if (i in l) == False:
        print(i)
        t = i
        while t <= 10000:
            t=d(t)
            if (t in l) == False:
                l.insert(len(l),t)
    else:
        continue
        
"""
2021.5.18
636ms, 29028kb
"""
def d(n):
    d = list(map(int,str(n)))
    k = n
    for i in d:
        k = k+i
    return k
l = []
for i in range(1,10001):
    if (i in l) == False:
        print(i)
    t=d(i)
    l.insert(len(l),t)
    
"""
The first one is much slower then the second one, although the root idea for solving is the same.
The reason is, the first one does many unmeaningful searching of a list
even though the first algorithm makes the list that are not self numbers without duplicate and in order
it does a lot of element searching, especially in the while loop.
However, although the second algorithm makes a list with lots of duplicates and unordered 'not' self numbers
it doesn't do a lot of element searching.
We don't need to concern about having duplicates and unordered set(of course the memory matters, but it can be solved easily actually)
"""
