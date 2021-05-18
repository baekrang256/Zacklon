"""
2021.5.18
28776kb, 88ms

used f-string formatting and chr() method that converts integer to the corresponding ASCII character
"""

s = input()
l = ''
for i in range(0,26):
    a = str(s.find(chr(i+97)))
    l = f"{l+a} "
print(l)
