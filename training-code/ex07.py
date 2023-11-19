from ex06 import max_days


if __name__ == '__main__':
    m = int(input('Enter month: '))
    y = int(input('Enter year: '))

    mx = max_days(m, y)

    print(f'Max days in {m}/{y} is {mx}')
