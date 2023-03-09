#Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.

import re
text = input()
pattern = "a.+b$"
x = re.search(pattern, text)
print(x)