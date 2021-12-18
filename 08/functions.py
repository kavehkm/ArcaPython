def all_contacts(contacts):
    if not contacts:
        print('no contacts!')
    else:
        for contact_id, record in contacts.items():
            print(contact_id, record['first_name'], record['last_name'])


def add(contacts):
    # generate new contact_id
    contact_id = len(contacts) + 1
    # get remain required info from user
    first_name = input('first name: ')
    last_name = input('last name: ')
    tel = input('tel: ')
    address = input('address: ')
    # create record
    record = {
        'first_name': first_name,
        'last_name': last_name,
        'tel': tel,
        'address': address
    }
    # add created record into contacts
    contacts[str(contact_id)] = record
    # tell user about success
    print('new contact added successfully')


def remove(contacts):
    contact_id = input('enter id of contact you want to remove: ')
    if contact_id in contacts:
        del contacts[contact_id]
        print('contact removed successfully')
    else:
        print('sry, contact with id {} does not exits'.format(contact_id))


def update(contacts):
    contact_id = input('enter id of contact you want to update: ')
    if contact_id in contacts:
        record = contacts[contact_id]
        first_name = input('first name: ') or record['first_name']
        last_name = input('last name: ') or record['last_name']
        tel = input('tel: ') or record['tel']
        address = input('address: ') or record['address']
        # update record by user entered values
        record['first_name'] = first_name
        record['last_name'] = last_name
        record['tel'] = tel
        record['address'] = address
        # tell user about success
        print('contact with id {} updated successfully'.format(contact_id))
    else:
        print('sry, contact with id {} does not exits'.format(contact_id))


def details(contacts):
    contact_id = input('enter id of contact: ')
    if contact_id in contacts:
        record = contacts[contact_id]
        for key, value in record.items():
            print(key, ':', value)
    else:
        print('contact with id {} does not exists'.format(contact_id))
