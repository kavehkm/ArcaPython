# define a list
# - method 1
mylist = [10, 66, 1.66, None, 'kaveh', True]
# - method 2
mylist = list(10, 66, 1.66, None, 'kaveh', True)


# indexing
#  >    >   >   >   >   >   >   >   >
#  0   1   2     3      4       5
# [10, 66, 1.66, None, 'kaveh', True]
#  -6  -5  -4    -3     -2      -1
#  <    <   <   <   <   <   <   <   <


# access to list members
mylist[1]   # 66
mylist[5]   # True
mylist[-4]  # 1.66


# edit list
mylist[2] = 'new value'
mylist[4] = 1+10j


# remove a member by index
del mylist[3]
del mylist[-2]


# get number of members in the list
len(mylist)


# slice list
mylist[2:]  # ['new value', True]
mylist[:2]  # [10, 66]
mylist[1:3] # [66, 'new value']


# check membership
'new value' in mylist   # True
'kaveh' in mylist       # False


# join lists
list1 = [1, 2, 3]
list2 = ['kaveh', 'darya']
list3 = ['C++', 'Python']
new_list = list1 + list2 + list3 # [1, 2, 3, 'kaveh', 'darya', 'C++', 'Python']


# list methods
list1 = [1, 2, 3, 4]
list2 = ['a', 'b', 'c']
list3 = ['x', 'y', 'x', 'y', 'z']

# append
list1.append('5')       # [1, 2, 3, 4, 5]
# clear
list1.clear()           # []
# count
list3.count('x')        # 2
# extend
list1.extend(list2)     # ['a', 'b', 'c']
# index
list2.index('b')        # 1
# insert
list1.insert(1, '*')    # ['a', '*', 'b', 'c']
# pop
list2.pop()             # ['a', 'b']    ---> 'c'
list2.pop(0)            # ['b']         ---> 'a'
# remove
list1.remove('a')       # ['*', 'b', 'c']
# reverse
list3.reverse()         # ['z', 'y', 'x', 'y', 'x']
# sort
list3.sort()            # ['x', 'x', 'y', 'y', 'z']
