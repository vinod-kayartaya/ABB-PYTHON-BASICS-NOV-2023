"""
List slice operations
"""


def main():
    nums = [25, 3, 45, 67, 89, 13, 84, 18, 3, 67, 12]
    print(f'nums is {nums}')
    # index operations
    print(f'element at index 6 is {nums[6]}')
    print(f'element at index 10 is {nums[10]}')
    print(f'element at index -1 is {nums[-1]}')
    print(f'element at index -5 is {nums[-5]}')

    # slice operations
    sub_nums = nums[3:7]
    print(f'`sub_nums` is {sub_nums}')
    sub_nums = nums[0:7]
    print(f'`sub_nums` is {sub_nums}')
    sub_nums = nums[:7]
    print(f'`sub_nums` is {sub_nums}')
    sub_nums = nums[4:len(nums)]
    print(f'`sub_nums` is {sub_nums}')
    sub_nums = nums[4:50000]
    print(f'`sub_nums` is {sub_nums}')
    sub_nums = nums[4:]
    print(f'`sub_nums` is {sub_nums}')

    # str as a list
    some_text = 'my name is vinod'
    print(f'some_text[:10] = `{some_text[:10]}`')
    print(f'some_text[11:] = `{some_text[11:]}`')
    some_list = []
    some_list += 'vinod'
    print(f'some_list is `{some_list}`')
    print(f'some_text[::-1] is `{some_text[::-1]}`')

    # more slice operations
    print(f'nums is `{nums}`')
    print(f'nums[:] is `{nums[:]}`')
    print(f'nums[::2] is `{nums[::2]}`')
    print(f'nums[1::2] is `{nums[1::2]}`')
    print(f'nums[::-1] is `{nums[::-1]}`')


if __name__ == '__main__':
    main()
