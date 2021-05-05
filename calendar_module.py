import calendar
import datetime
import  time

print(calendar.weekheader(3))
print()
print(calendar.firstweekday())

day_of_the_week = calendar.weekday(2021, 5, 5)
print(day_of_the_week)

print(calendar.isleap(2021))
print(calendar.leapdays(2020, 2025))
