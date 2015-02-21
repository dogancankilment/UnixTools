def fibo_loop(n):
    """
    Fibonacci calculation loop format
    """

    a, b = 0, 1

    for i in range(0, n):
        a, b = b, a + b

    return a


def fibo_recursive(n):
    """
    Fibonacci calculation recursive format
    """

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo_recursive(n-1) + fibo_recursive(n-2)


if __name__ == '__main__':
    pass