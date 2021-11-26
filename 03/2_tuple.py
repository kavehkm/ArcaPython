# define a tuple
# - method 1
mytuple = ('True', True, 'False', 0, 0.0)
# - method 2
mytuple = ('True', True, 'False', 0, 0.0)


# access to tuple members
mytuple[1]  # True
mytuple[2]  # 'False'
mytuple[-1] # 0.0


# edit tuple ???!
    # you cannot change tuple


# remove a member by index ???!
    # ...


# get number of members in tuple
len(mytuple)


# slice tuple
mytuple[2:]     # ('False', 0, 0.0)
mytuple[:2]     # ('True', True)
mytuple[1:3]    # (True, 'False')


# check membership
'True' in mytuple   # True
5 in mytuple        # False


# join tuples
tuple1 = ('a', 'b', 'c')
tuple2 = ('x', 'y', 'z')
new_tuple = tuple1 + tuple2 # ('a', 'b', 'c', 'x', 'y', 'z')


# tuple methods
test_tuple = ('1', 1, 2, '1', '1', 'x')

# count
test_tuple.count('1')   # 3
# index
test_tuple.index('x')   # 5
test_tuple.index('1')   # 0
