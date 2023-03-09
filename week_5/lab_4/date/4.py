#Write a Python program to calculate two date difference in seconds.

from datetime import timedelta, datetime
 
now = datetime.now()
date1 = datetime(2023, 1, 22)
date2 = datetime(2023, 1, 28)
dif = date2-date1
dif2 = now-date1
print(dif.total_seconds())

print(dif2.total_seconds())