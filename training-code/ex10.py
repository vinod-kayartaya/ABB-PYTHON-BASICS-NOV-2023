from ex09 import is_prime


def print_primes_between(start: int, end: int) -> None:
    n = start
    while n <= end:
        if is_prime(n):
            print(n, end=', ')
        n += 1
    print()


if __name__ == '__main__':
    first = int(input('Enter the first number: '))
    last = int(input('Enter the last number: '))
    print_primes_between(first, last)
