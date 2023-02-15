
year = int(input('Year: '))
month = int(input('Month: '))
day = int(input('Day: '))

if year >= 1900 and (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12) and (1 <= day <= 31):
    print(f'{day}/{month}/{year} - zi valida')
elif year >= 1900 and (month == 4 or month == 6 or month == 9 or month == 11) and (1 <= day <= 30):
    print(f'{day}/{month}/{year} - zi valida')
elif year >= 1900 and month == 2 and (1 <= day <= 28):
    print(f'{day}/{month}/{year} - zi valida')
# elif (year == (2000 % 400 == 0)) and month == 2 and (1 <= day <= 29):
#     print(f'{day}/{month}/{year} - an bisect, zi valida')
else:
    print('data invalida!')
