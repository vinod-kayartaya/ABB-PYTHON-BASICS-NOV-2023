"""
Example of a `while` loop
"""


def main():
    n = input('Enter a number: ')
    if not n.isdigit():
        print('The input is not a number')
        exit(1)

    n = int(n)
    i = 1
    while i <= 10:
        print(f'{n} X {i} = {n*i}')
        i += 1


if __name__ == '__main__':
    main()
