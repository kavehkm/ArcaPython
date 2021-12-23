# define a set
# - method 1
thisset = {1, 2, 3, 3, 4, 'kaveh'}          # {1, 2, 3, 4, 'kaveh'}
# - method 2
thisset = set([1, 2, 3, 3, 4, 'kaveh'])     # {1, 2, 3, 4, 'kaveh'}


# access to set members ???!
    # you cannot access set members by index


# edit set ???!
    # you cannot edit set members directly!(cause of direct access problem)


# remove a member by index ???!
    # yo...cnt...


# slice set ???!
    # yo...cnt...sli...set..!(cau...of...dir...acc)


# get number of members in the set
len(thisset)


# check membership
'kaveh' in thisset  # True
3.1415 in thisset   # False


# set methods
s1 = {1, 2, 3, 4, 5}
s2 = {3, 4, 5, 6, 7}
s3 = {3.14, 2.67, 1, 7, 3, 5, None, 2, 4, 6}
s4 = {'kaveh', 0.066, 6.6}

# add
s4.add(2.626066)                # {'kaveh', '0.066, 6.6, 2.626066}
# clear
s4.clear()                      # {}
# difference
s1.difference(s2)               # {1, 2} change
# discard
s1.discard(5)                   # {1, 2, 3, 4}
s1.discard(10)                  # {1, 2, 3, 5} 
# remove
s1.remove(4)                    # {1, 2, 3}
s1.remove(10)                   # raise error!
# intersection
s1.intersection(s2)             # {3, 4, 5} change
# union
s1.union(s2)                    # {1, 2, 3, 4, 5, 6, 7}
# issubset
s1.issubset(s3)                 # True
s1.issubset(s2)                 # False
# issuperset
s3.issuperset(s1)               # True
s1.issuperset(s2)               # False
# symmetric_difference
s1.symmetric_difference(s2)     # {1, 2, 4, 5, 6, 7}
