def square(n):
    print('squre function called from module2')
    return n * n


def cube(n):
    print('cube function called from module2')
    return n * n * n


def factorial(x):
    print('factorial function called from module2')
    s = 1
    for i in range(1, x + 1):
        s *= i
    return s
