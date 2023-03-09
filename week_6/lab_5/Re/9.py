#Write a Python program to insert spaces between words starting with capital letters.
import re
text = input()
text1 = re.sub('(?<!\s)(?=[A-Z])', ' ', text)

print(text1)
