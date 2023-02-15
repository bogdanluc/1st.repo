import datetime
from datetime import date
an = int(input('year:'))
luna = int(input('luna: '))
zi = int(input('day: '))
data = datetime.date(an, luna, zi)
print(data.weekday())





