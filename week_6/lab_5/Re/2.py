#Write a Python program that matches a string that has an 'a' followed by two to three 'b'.

import re

text = input()
pattern = "a{1}b{2,3}"
x = re.search(pattern, text)
print(x)