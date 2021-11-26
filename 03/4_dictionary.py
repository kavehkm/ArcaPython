# define a dictionary
# - method 1
mydict = {'a': 1, 'b': 2, 'name': 'kaveh', 'tel': '0937'}
# - method 2
mydict = dict(a=1, b=2, name='kaveh', tel='0937')


# access to dictionary by keys
mydict['a']     # 1
mydict['tel']   # '0937'


# edit dictionary
mydict['name'] = 'darya'    # {'a': 1, 'b': 2, 'name': 'darya', 'tel': '0937'}


# remove a member by key
del mydict['b']     # {'a': 1, 'name': 'darya', 'tel': '0937'}


# get number of key-value pairs in the dictionary
len(mydict)     # 3


# check key membership
'name' in mydict    # True
'address' in mydict # False


# add new key-value pair into dictionary
mydict['new_key'] = 'new_value' # {'a': 1, 'name': 'darya', 'tel': '0937', 'new_key': 'new_value'}


# dictionary methods
d1 = {
    'a': 1,
    'b': 2,
    'c': '3',
    'k1': True
}
d2 = {
    'id': 66,
    'name': 'kaveh',
    'address': 'mashhad',
    'happy': True
}

# get
d1.get('a')         # 1
d1.get('x')         # None
d1.get('x', '404')  # 404
# items
d1.items()          # [('a', 1), ('b', 2), ('c', '3'), ('k1', True)]
# keys
d1.keys()           # ['a', 'b', 'c', 'k1']
# values
d1.values()         # [1, 2, '3', True]
# pop
d1.pop('k1')        # {'a': 1, 'b': 2, 'c': '3'} ---> True
# popitem
d1.popitem()        # {'a': 1, 'b': 2} ---> ('c', '3')
# update
d1.update(d2)       # {'a': 1, 'b': 2, 'id': 66, 'name': 'kaveh', 'address': 'mashhad', 'happy': True}
# clear
d1.clear()          # {}
