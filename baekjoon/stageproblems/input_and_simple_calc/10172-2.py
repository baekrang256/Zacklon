
"""
DATE : 2021.03.14
"""

"""
THIS IS NOT A SOLUTION
I thought about the way of solving the problem another way while seeing the link below
https://wikidocs.net/13
It is said that you can print the string value with several lines by using """."""
So I applied that, but baekjoon didn't accepted it because of the following reason.
'출력 형식이 잘못되었습니다'
However, if you compile it, it is correct.
Question about '출력 형식' exists in baekjoon. Look at the following link
https://www.acmicpc.net/problem/5177
I think the reason baekjoon is not accepting this answer is somewhat related to the 'newline error' that was mentioned at the below link.
https://www.acmicpc.net/board/view/4993
However this is not certain. It's just my guess.
I'm guessing that if we use this idea, we have to make several new lines, and this may effect to the reason why baekjoon don't accept the answer.
"""

multiline = '''
|\_/|
|q p|   /}
( 0 )"""\\
|"^"`    |
||_/=\\\\__|
'''
print(multiline)
