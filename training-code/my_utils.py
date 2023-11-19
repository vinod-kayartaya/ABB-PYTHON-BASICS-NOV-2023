def dir2(obj):
    """
    A custom method to get the list of non-dunder attributes
    To use this:

    make sure you are in your working directory, before launching the python shell

    from my_utils import dir2
    dir2(list)

    OR

    import my_utils
    my_utils.dir2(list)

    :param obj:
    :return: list of all non-dunder attributes of obj
    """
    atrs = [at for at in dir(obj) if not at.startswith('_')]
    return atrs


def factorial(num: int) -> int:
    f = 1
    for n in range(num, 1, -1):
        f *= n
    return f


if __name__ == '__main__':
    # attributes = dir2(str)
    # print(attributes)
    print(factorial(5))
