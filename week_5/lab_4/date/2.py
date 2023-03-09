#Write a Python program to print yesterday, today, tomorrow.

from datetime import datetime, timedelta

now = datetime.date(datetime.now())
x = timedelta(days=1)

print("Yesterday:",now-x)
print("Today:",now)
print("Tomorrow:",now+x)
