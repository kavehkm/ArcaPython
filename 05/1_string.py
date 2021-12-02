# define string
# - method 1
first_name = 'kaveh'

# - method 2
last_name = "mehrbanian"

# - method 3(multi-line)
bio = '''this is
about me
'''

# - method 4(multi-line)
description = """some description
about kaveh mehrbanian
"""


# access characters in string
first_name[1]   # 'a'
first_name[3]   # 'e'
bio[-2]         # 'm'


# edit string???!
    # you cannot change string


# remove a character by index from string???!
    # you ...


# get number of characters in string
len(bio)


# slice string
first_name[2:]      # 'veh'
bio[:3]             # 'thi'
description[2:5]    # 'me '


# check substring in string
'about' in bio          # True
'xi' in description     # False


# concat strings
first_name + ' ' + last_name    # 'kaveh mehrbanian'


# format strings
# - method 1
'hello %s' % first_name         # 'hello kaveh'
# - method 2
'hello {}'.format(first_name)   # 'hello kaveh'
# - method 3
f'hello {first_name}'           # 'hello kaveh'


# string methods
hello_string = 'Hello wOrld'

# lower
hello_string.lower()                    # 'hello world'
# upper
hello_string.upper()                    # 'HELLO WORLD'
# capitalize
hello_string.capitalize()               # 'Hello world'
# title
hello_string.title()                    # 'Hello World'
# swapcase
hello_string.swapcase()                 # 'hELLO WoRLD'
# count
hello_string.count('o')                 # 2
# encode
encoded_hello = hello_string.encode()   # b'Hello wOrld'
# decode
encoded_hello.decode()                  # 'Hello wOrld'
# find
hello_string.find('wO')                 # 6
# startswith
hello_string.startswith('H')            # True
hello_string.startswith('x')            # False
# endswith
hello_string.endswith('ld')             # True
hello_string.endswith('bye')            # False
# join
'-'.join(['kaveh', 'mehrbanian'])       # 'kaveh-mehrbanian'
# split
'keveh-mehrbanian'.split('-')           # ['kaveh', 'mehrbanian']
# rsplit
'Recipient.V1.64.exe'.split('.')        # ['Recipient', 'V1', '64', 'exe']
'Recipient.V1.64.exe'.rsplit('.', 1)    # ['Recipient.V1.64', 'exe']
'Recipient.V1.64.exe'.rsplit('.', 2)    # ['Recipient.V1', '64', 'exe']
# splitlines
'hello\nworld\nsalam'.splitlines()      # ['hello', 'world', 'salam']
# strip
'   hello   '.strip()                   # 'hello'
# rstrip
'   hello   '.rstrip()                  # '   hello'
# lstrip
'   hello   '.lstrip()                  # 'hello   '
# isdigit
'66565'.isdigit()                       # True
'hello'.isdigit()                       # False
# isdecimal
'66.6'.isdecimal()                      # False
'986'.isdecimal()                       # True
# isalpha
'xyzabc'.isalpha()                      # True
'$%abcxyz'.isalpha()                    # False
# islower
'Hello'.islower()                       # False
'hello'.islower()                       # True
