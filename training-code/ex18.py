"""
Example for handling runtime errors

This program is supposed to be executed from CLI by passing arguments.

For example:

python ex18.py 123 45

Here `python` is the program executed by the OS and 'ex18.py', '123', and '45'
are the command line arguments passed to the actual command `python`
"""

import sys


def main():
    try:
        arg1 = sys.argv[1]
        arg2 = sys.argv[2]
        num = int(arg1)
        den = int(arg2)
        quot = num // den
        rem = num % den
        print(f'{num}/{den} yields to a quotient of {quot} and a remainder of {rem}')
    except IndexError:
        print(f'2 integers were expected, but got {len(sys.argv)-1}')
    except ZeroDivisionError:
        print(f'Cannot divide {arg1} by zero')
    except ValueError:
        print('Only integers were expected')
        exit(13)
    except Exception as err:
        print(f'OOPS! something went wrong - {err}')
    finally:
        print('this is executed at all scenarios')


if __name__ == '__main__':
    main()
    print('end of the script execution')
