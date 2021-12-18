# standard
import os
# internal
import functions as fn


# global CONTACTS: hold all records
CONTACTS = dict()

# application menu
menu = [
    '1) list all contacts',
    '2) contact details',
    '3) add new',
    '4) remove contact',
    '5) update contact',
    'x) exit'
]


def print_menu():
    print('\n'.join(menu))


while True:
    # print menu to user
    print_menu()
    # get user response
    answer = input()

    # dispatch answer
    if answer == '1':
        fn.all_contacts(CONTACTS)
    elif answer == '2':
        fn.details(CONTACTS)
    elif answer == '3':
        fn.add(CONTACTS)
    elif answer == '4':
        fn.remove(CONTACTS)
    elif answer == '5':
        fn.update(CONTACTS)
    elif answer == 'x':
        print('Goodbye')
        break
    else:
        print('check menu and try again')
        continue
    # wait for user
    input('press any key continue...')
    # clear screen
    if os.name == 'posix':
        # linux
        os.system('clear')
    else:
        # windows
        os.system('cls')
