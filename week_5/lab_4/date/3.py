#Write a Python program to drop microseconds from datetime.

from datetime import datetime

x = datetime.now()
print(x.strftime("%Y-%m-%d %I:%M:%S"))


