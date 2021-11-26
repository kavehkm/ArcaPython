# define a while:
# while conditions:
#   execute instructions


# simple while for counting from 1 to 10
counter = 1
while counter < 11:
    print('counter is', counter)
    counter += 1


# use while to iterate through iterables(list, tuple)
testlist = ['kaveh', 'darya', 'ahmad', 'arash']
index = 0
while index < len(testlist):
    print('index is', index)
    print('value at index', index, 'is', testlist[index])
    index += 1


# define a for
# for index in range(start_index, stop_index, step):
#   execute instructions


# simple for to counting from 1, 10
for i in range(1, 11, 1):
    print(i)


# use for to iterate through iterables(list, tuple, set and dictionary)
testlist = ['a', 'b', 'c', 'd']
for i in testlist:
    print(i)

testuple = ('x', True, None, False, 'y')
for j in testuple:
    print(j)

testset = {'kaveh', 66, 66, 66, '66'}
for member in testset:
    print(member)

testdict = {'a': 1, 'b': 2, 'c': 3, 'x': 22, 'y': 24}
for key, value in testdict.items():
    print(key, value)
