"""
2021.3.28
28776kb,76ms

I thought about two ways to find maximum value in the list.
First one is, we append the value into the list
then we find the max value, and return the index of the max value using index() method.
However it wouldn't really have a point of doing this compared to the first solution that I come up with without the list.

The second one is the below algorithm
We used the method max()
https://www.tutorialspoint.com/python/list_max.htm
This method was not mentioned in the Data Structures at python documents.
https://docs.python.org/3/tutorial/datastructures.html
The above link was the link that I tried to find the method max() for list, but I wasn't able to do that...
by appending all the numbers in the list, using max method will simply find the max value in the list.
Since every value in the list is distinct we don't really have to think about the case for duplicate max numbers.
After finding max value, we just use the index method to find the place where the max number exists!
"""

import sys
lofn = []
for i in range(9):
    lofn.append(int(sys.stdin.readline()))
print(max(lofn))
print(lofn.index(max(lofn))+1)
