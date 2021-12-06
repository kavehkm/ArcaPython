# internal
import module2 as m # set alias `m` for module2


variable1 = 'variable1 in module1'

variable2 = 'variable2 in module1'


def func1():
    print('func1 called from module1')


def func2(x, y):
    print('func2 called with {} and {} from module1'.format(x, y))


def func3(z):
    print('func3 called with {} from module1'.format(z))
    print('square of {} is {}'.format(z, m.square(z)))
    print('cube of {} is {}'.format(z, m.cube(z)))
    print('factorial of {} is {}'.format(z, m.factorial(z)))
