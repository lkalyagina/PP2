#Write a Python program to split a string at uppercase letters.

import re
text = input()
pattern = "[A-Z]"
x = re.split(pattern, text)
print(x)
