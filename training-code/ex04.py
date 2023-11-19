"""
This example prints the number of days in a given month/year.

If the month or year is invalid, an error message is displayed
"""

year = int(input('Enter a year (>=1900): '))

if year < 1900:
    print(f'You entered {year} for year, which invalid. Year must be >= 1900')
    exit(1)

month = int(input('Enter a month (1-12): '))

if month < 1 or month > 12:
    print(f'You entered {month} for month, which is invalid. Month should be between 1 and 12')
    exit(2)

if month == 2:
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        print(f'There are 29 days in the month {month} of year {year}')
    else:
        print(f'There are 28 days in the month {month} of year {year}')
elif month in [4, 6, 9, 11]:
    print(f'There are 30 days in the month {month} of year {year}')
else:
    print(f'There are 31 days in the month {month} of year {year}')
