"""
Different kinds of function parameters (aka arguments) in Python
"""


def calculate_sum(*args):
    print(f'type of args is {type(args)} and args is {args}')
    args = [n for n in args if type(n) in (int, float)]
    print(f'type of args is {type(args)} and args is {args}')
    return sum(args)


def print_info(**kwargs):
    print(f'type of kwargs is {type(kwargs)}')
    print(f'value of kwargs is {kwargs}')
    if 'firstname' not in kwargs:
        print('No firstname found!')
        return
    print(f'Name    = {kwargs["firstname"]} {kwargs.get("lastname", "")}')
    print(f'Age     = {kwargs.get("age", 20)} years')
    print(f'Married = {kwargs.get("married", False)}')
    print(f'Email   = {kwargs.get("email", "")}')
    print('-'*80)


def process_data(firstname=None, email=None):
    print(f'Firstname = {firstname}')
    print(f'Email     = {email}')
    print('-'*80)


def is_decimal(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def to_float(s):
    try:
        return float(s)
    except ValueError:
        return 0.0


if __name__ == '__main__':
    total = calculate_sum(10, 20, 30, 'vinod', 2.2, 18)
    print(f'total = {total}')

    print_info(firstname='Vinod', lastname='Kumar', age=50, married=True)
    print_info(firstname='Rahul', lastname='Varma', email='rahul@xmpl.com')

    d1 = dict(firstname='Rohit', email='rohit@xmpl.com')
    print_info(**d1)
    process_data(**d1)

    user_data = input('Enter numbers separated using space: ')
    user_data = user_data.split(' ')
    user_data = [to_float(n) for n in user_data]
    total = calculate_sum(*user_data)
    print(f'total = {total}')
