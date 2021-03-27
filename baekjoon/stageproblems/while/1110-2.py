"""
2021.3.27
28776kb, 76ms

if we use input, we don't need to be concerned about the string having '\n'
of course input() is less efficient then readline, but since we only use input() once, it doesn't really matter.
We used join instead of '+=' because we will need to use a lot of concentration while doing this loop
+= is less efficient than join for lots of concentration.
Look at the link below for more explanation.
https://stackoverflow.com/questions/39675898/is-python-string-concatenation-bad-practice
as the first solution, we used string, since integer types are not iterable.
"""

n = input()
t = int(n)
i = 0

while True:
    i += 1
    if int(n)<10:
        n = ''.join([n,n])
    else:
        k = str(int(n[0])+int(n[1]))
        if len(k) == 1:
            n = n[1]+k
        else:
            n = n[1]+k[1]
        if n[0] == '0':
            n = n[1]
    if t == int(n):
        break
print(i)
