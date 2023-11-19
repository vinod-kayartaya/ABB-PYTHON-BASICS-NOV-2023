"""
This is an example for understanding the `list` object
"""


def main():
    numbers = [12, 3, 45, 67, 89, 13, 84, 18, 3, 67, 12]
    print(f'there are {len(numbers)} elements in the list `numbers`')
    print(f'the element at index 5 in `numbers` is {numbers[5]}')
    numbers.append('vinod')
    print(f'`numbers` = {numbers}')
    numbers.insert(0, 'kumar')
    print(f'`numbers` = {numbers}')
    numbers.insert(1000000, 560)
    print(f'`numbers` = {numbers}')
    num_to_insert = 3
    if num_to_insert in numbers:
        idx = numbers.index(num_to_insert)
        numbers.insert(idx, 999)
        print(f'`numbers` = {numbers}')

    print(f'34 appears {numbers.count(34)} times in `numbers`')

    # remove the last element from the list
    for _ in range(3):
        popped_elem = numbers.pop()
        print(f'popped element is {popped_elem} and the `numbers` is {numbers}')

    # remove the first element from the list
    for _ in range(3):
        first_elem = numbers.pop(0)
        print(f'the removed element is {first_elem} and the `numbers` is {numbers}')

    # remove a specific element by its value
    num_to_remove = 89
    if num_to_remove in numbers:
        numbers.remove(num_to_remove)
        print(f'after removing {num_to_remove}, the `numbers` is {numbers}')

    numbers.reverse()
    print(f'after reversing the `numbers` is {numbers}')

    numbers.sort()
    print(f'after sorting the `numbers` is {numbers}')

    another_numbers_list = [99, 88, 77]
    numbers.extend(another_numbers_list)
    print(f'`numbers` is {numbers}')
    another_numbers_list = [66, 55, 44]
    numbers += another_numbers_list
    print(f'`numbers` is {numbers}')


if __name__ == '__main__':
    main()
