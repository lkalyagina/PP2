#Write a Python program to convert a given camel case string to snake case.

import re
text = input()
text = text[0].lower() + text[1:]
pattern = "_"

for i in text:
    if i.isupper():
        text = re.sub(i, pattern, text)