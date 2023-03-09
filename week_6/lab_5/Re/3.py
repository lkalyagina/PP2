#Write a Python program to find sequences of lowercase letters joined with a underscore.
import re

text = input()
pattern = "[a-z]*_.*"
x = re.findall(pattern, text)
print(x)