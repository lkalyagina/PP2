#Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.

import re
text = input()
pattern = "ab*"
x = re.search(pattern, text)
print(x)