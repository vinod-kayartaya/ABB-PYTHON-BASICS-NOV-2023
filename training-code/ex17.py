"""
Different ways of reading text files
"""

filename = input('Enter the filename to open and read: ')


def file_read_method1():
    with open(filename, 'rt') as file:
        content = file.read()
    print(content)


def file_read_method2():
    file = open(filename, 'rt')
    while True:
        one_line = file.readline()
        if one_line == '':  # reached the end of the file
            break
        print(one_line, end='')

    file.close()


def file_read_method3():
    # using a context manager, we do not have to worry about resource leaks
    with open(filename) as file:
        all_lines = file.readlines()  # returns a `list`
    # at this place, `file` is already closed

    for one_line in all_lines:
        print(one_line, end='')


def file_read_method4():
    with open(filename) as file:
        for one_line in file:
            print(one_line, end='')


def main():
    file_read_method4()


if __name__ == '__main__':
    main()
