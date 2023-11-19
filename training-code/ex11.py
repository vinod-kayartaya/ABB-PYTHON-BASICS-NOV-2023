"""
Using `for` loop
"""


def main():
    for user_name in ('Vinod', 'Shyam', 'Rohit', 'Virat', 'Vinod', 'Shyam'):
        print(f'name is {user_name}')

    for i in range(10):
        print(f'value of i is {i}')

    for i in range(10):
        for j in range(i+1):
            print(j, end=' ')
        print()


if __name__ == '__main__':
    main()
