"""
2021.3.28
28776kb,64ms

Interesting solution.
We first make a list with 42 0 element
([..]*int makes a list with int number of [..], see the following link : https://wikidocs.net/14#_11)
then we get a remainder of each 10 numbers, and increas the number in the list with the position that is same as the remainder.
Then the counter k, counts the number of different remainders by counting the number of index with element large or equal to 1.
Having a really long list, and also having a for statement repeated 42 times is pretty inefficient both in space and time, but it is interesting, ya know.
"""

N= [0] * 42
for i in range(10):
  a = int(input())
  N[a%42] += 1
k =0
for i in N:
  if i >= 1:
    k+=1

print(k)
