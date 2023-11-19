"""
An example for understanding `list comprehension`
"""


def main():
    nums = [25, 3, 46, 67, 89, 13, 84, 18, 3, 67, 12]
    print(f'nums is {nums}')

    # create a new list consisting of only even numbers from `nums`
    even_nums = []
    for n in nums:
        if n % 2 == 0:
            even_nums.append(n)
    print(f'even_nums is {even_nums}')

    # using list comprehension
    even_nums = [n for n in nums if n % 2 == 0]
    print(f'even_nums is {even_nums}')

    odd_nums = [num for num in nums if num % 2]
    print(f'odd_nums is {odd_nums}')

    squares = [n*n for n in nums]
    print(f'squares is {squares}')

    names = ['Vinod', 'Shyam', 'Anand', 'Keller']
    codes = [remove_vowels(name).upper() for name in names]
    print(f'names is {names}')
    print(f'codes is {codes}')


def remove_vowels(s):
    return ''.join([c for c in s if c.lower() not in 'aeiou'])


if __name__ == '__main__':
    main()
