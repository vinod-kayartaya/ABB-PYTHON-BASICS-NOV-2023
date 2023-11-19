def is_leap(year: int) -> bool:
    if type(year) is not int:
        raise TypeError('Year must be an int')

    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


def is_valid_month(month: int) -> bool:
    return 1 <= month <= 12


def max_days(month: int, year: int) -> int:
    if not is_valid_month(month):
        raise ValueError('Month must be between 1 and 12')
    if year < 1900:
        raise ValueError('Year must be >= 1900')

    if month == 2:
        return 29 if is_leap(year) else 28
    elif month in (4, 6, 9, 11):
        return 30
    else:
        return 31


if __name__ == '__main__':
    y = int(input('Enter a number for year: '))
    ans = 'Yes' if is_leap(y) else 'No'

    print(f'{y} is a leap year? {ans}')
