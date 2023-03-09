#Write a Python program to convert a given camel case string to snake case.

import re
text = input()
text = text[0].lower() + text[1:]
pattern = "_"
text2 = re.sub(r'(?<!^)(?=[A-Z])', '_', text).lower()
print(text2)