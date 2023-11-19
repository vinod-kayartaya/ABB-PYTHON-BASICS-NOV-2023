def is_prime(num: str) -> bool:
    i = 2
    while i < num:
        if num % i == 0:
            return False
        i += 1
    return True


def main():
    n = input('Enter a number: ')
    if n.isdigit():
        n = int(n)
        print(f'Is {n} a prime? {is_prime(n)}')


if __name__ == '__main__':
    main()
