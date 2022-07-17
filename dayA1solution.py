from datetime import date
import calendar

date = date.today()
day_today = calendar.day_abbr[date.weekday()]
if day_today == 'Sun':
    fare = 80
elif day_today == 'Sat':
    fare = 60
else:
    fare = 100
print(f'Date:{date.strftime("%Y-%m-%d")}')
print(f'Day:{day_today}')
print(f'Fare:{fare}')

