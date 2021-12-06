# define and call functions


# - without arguments and return value(None returned)
def welcome():
    print('welcome bro')
# - call
welcome()   # 'welcome bro'


# - without return value(None returned)
def welcome(name):
    message = 'welcome bro {}'.format(name)
    print(message)
# - call
welcome('kaveh')    # 'welcome bro kaveh'
# ~ call
friend = 'amin'
welcome(friend)     # 'welcome bro amin'


# with argument and return value
def welcome(name):
    message = 'welcome bro {}'.format(name)
    return message
# - call
result = welcome('kaveh')
print(result)       # 'welcome bro kaveh'


# with positional and optional arguments
def welcome(name, message='welcome bro'):
    message = '{} {}'.format(name, message)
    return message
# - call
result = welcome('kaveh', 'welcome dear')
print(result)       # 'welcome dear kaveh'
# ~ call
result = welcome('kaveh')
print(result)       # 'welcome bro kaveh'


# return more than just one value!
def circle_compute(radius):
    area = 3.1415 * radius ** 2
    environment = 2 * 3.1415 * radius
    return area, environment
# - call
e, a = circle_compute(4)
print(e, a)         # 25.132 50.264


# packing
# - limited args
def summer(a, b, c, d, e, f, G):
    result = a + b + c + d + e + f + G
    return result
# - call
print(summer(1, 10, 100, 101, 100, 10, 1))      # 323

# - unlimited args
def summer(*numbers):
    s = 0
    for number in numbers:
        s += number
    return s
# - call
print(summer(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))    # (1 + 10) * 5 =  55


# unpacking
def summer(a, b, c, d, e, f, G):
    result = a + b + c + d + e + f + G
    return result
# - call
numbers = [6, 5, 4, 3, 2, 1, 7]
r = summer(
    numbers[0],
    numbers[1],
    numbers[2],
    numbers[3],
    numbers[4],
    numbers[5],
    numbers[6]
    )
print(r)                # 28
# ~ call
numbers = [6, 5, 4, 3, 2, 1, 7]
print(summer(*numbers)) # 28


# packing and unpacking
def average(*marks):
    s = sum(marks)
    count = len(marks)
    return s / count
# - call
students_marks = [18, 10, 12, 19, 20, 19.99]
print(average(*students_marks)) # 16.498333333


# TODO: keyword pack and unpack