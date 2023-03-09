#Write a Python program to subtract five days from current date.

from datetime import datetime, timedelta

x = datetime.now() 
y = timedelta(days=5)
print(x)
print(y)
print(x-y)