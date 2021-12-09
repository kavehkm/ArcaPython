# define functions


###################################################
# without arguments and also without return value #
###################################################
# - define
def welcome():
    print('welcome bro')

# - call
welcome()


########################
# without return value #
########################
# - define
def welcome(name):
    message = 'welcome bro {}'.format(name)
    print(message)

# - call1
welcome('kaveh')
# - call2
friend = 'amin'
welcome(friend)


##################################
# with argument and return value #
##################################
# - define
def welcome(name):
    message = 'welcome bro {}'.format(name)
    return message

# - call
result = welcome('kaveh')
print(result)


##########################################
# with positional and optional arguments #
##########################################
# - define
def welcome(name, message='welcome bro'):
    message = '{} {}'.format(name, message)
    return message

# - call1
result = welcome('kaveh', 'welcome dear')
print(result)
# - call2
result = welcome('kaveh')
print(result)


####################################
# return more than just one value! #
####################################
# - define
def circle_compute(radius):
    area = 3.1415 * radius ** 2
    environment = 2 * 3.1415 * radius
    return area, environment

# - call
e, a = circle_compute(4)
print(e, a)


###########
# packing #
###########
# - limited args
def summer(a, b, c, d, e, f, G):
    result = a + b + c + d + e + f + G
    return result

# - call
print(summer(1, 10, 100, 101, 100, 10, 1))


# - unlimited args
def summer(*numbers):
    s = 0
    for number in numbers:
        s += number
    return s

# - call
print(summer(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


#############
# unpacking #
#############
# - define
def summer(a, b, c, d, e, f, G):
    result = a + b + c + d + e + f + G
    return result

# - call1
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
print(r)

# - call2
numbers = [6, 5, 4, 3, 2, 1, 7]
print(summer(*numbers))


#########################
# packing and unpacking #
#########################
# - define
def average(*marks):
    s = sum(marks)
    count = len(marks)
    return s / count

# - call1
students_marks = [18, 10, 12, 19, 20, 19.99]
print(average(*students_marks))


# TODO: keyword pack and unpack