"""
DATE : 2021-03-17
28776KB, 68ms
"""

"""
To understand this algorithm, you first need to understand the following.
https://dojang.io/mod/page/view.php?id=2405
https://dojang.io/mod/page/view.php?id=2286
The first link explains about an iterable object.
The second link explains about a function map(), which uses iterable objects as one type of input.

To briefly explain about map(), it is a function that returns a map object
map(int, input().split()) converts the input list into a map object in terms of integer.
A map object is also iterable, which means that it can be unpacked, or that we can use several variables to store each of the elements in the object map.

since the input is a string, it is an iterable object.
And function map() can be applied to all iterable objects.
however, the reason the first line still used the function split() is because when we just map the input and have first two characters be a and b,
variable b will store ' ', or blank.
that's why we use split function to the input function so that we can turn the string into list, deleting the blank.
Since the list is still an iterable object, it can apply the map function.

Of course we could also use the following code
i = input().split()
print(int(i[0])+int(i[1]))
This code is a little bit cumbersome compared to the below code since we have to change each of the variable into an integer.
We need to use a function int() since each of the element in i is a string.
"""

a, b = map(int, input().split())
print(a+b)
