"""
This is an example of using `if` statements.

Other related keywords are `else` and `elif`
"""

num = int(input('Enter a number for a month [1-12]: '))

print(f'You entered {num} for a month')

if num < 1 or num > 12:
    print('This is an invalid month')
    print('Month number should be between 1 and 12')
else:
    print('This is a valid month number')

