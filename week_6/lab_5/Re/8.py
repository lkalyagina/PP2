#Write a Python program to split a string at uppercase letters.

import re
text = input()
pattern = "[A-Z]"

text2 =re.findall(r'[a-zA-Z][^A-Z]*', text)

print()
