#Write a Python program to find the sequences of one upper case letter followed by lower case letters.

import re

text = input()
pattern = "[A-Z]{1}[a-z]*"
x = re.findall(pattern, text)
print(x)