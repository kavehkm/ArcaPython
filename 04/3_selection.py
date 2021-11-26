# falsy concepts and values
falsy_values = [
    # collections
    [],
    (),
    set(),
    dict(),
    # strings
    '',
    ''''''
    "",
    """""",
    # numbers
    0,
    0.0,
    0+0j,
    0-0j,
    0j,
    # constants,
    False,
    None
]


# truthy concepts and values
truthy_values = [
    # .
    # ..
    # ...
    # all possible values exclude falsy_values defined right before...
]


# use bool() function to determine a value is truthy or falsy:
bool(-1)
bool(None)
bool([])
bool(0.00001)


# if:
if 1 > 0:
    print('yes 1 is greater than 0')


# if-else:
if 1 > 2:
    print('yes 1 is greater than 2')
else:
    print('no 1 is lower than 2')


# if-elif-elif-...
if 1 > 2:
    print('yes 1 is greater than 2')
elif 1 > 3:
    print('yes 1 is greater than 3')
elif 1 > 0:
    print('yes 1 is greater than 0')
elif 1 > 4:
    print('yes 1 is greater than 4')


# if elif-elif-elif-...-elif-else
if 1 > 2:
    print('yes 1 is greater than 2')
elif 1 > 3:
    print('yes 1 is greater than 3')
elif 1 > 4:
    print('yes 1 is greater than 4')
elif 1 > 5:
    print('yes 1 is greater than 5')
else:
    print('no, 1 is lower than 2, 3, 4 and 5')
