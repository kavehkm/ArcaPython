# standard
import time
import math
import random
import string
# internal
import module1


# sleep
time.sleep(5)                       # go to sleep for 5 seconds
# stftime
t = time.strftime('%H:%M:%S')       # get current formatted time
print(t)

# ceil
print(math.ceil(4.3))                      # 5
# floor
print(math.floor(4.6))                     # 4
# sin
print(math.sin(90))                        # 0.89
# cos
print(math.cos(0))                         # 1.0
# PI
print(math.pi)                             # 3.14159265...
# e
print(math.e)                              # 2.782...



# random int
print(random.randint(1, 10))                # random int from [1, 2, 3, ..., 8, 9, 10]
# random choice from list
print(random.choice([5, 1, 2, 3, 4]))       # one choice from list


# ascii collection
print(string.ascii_letters)                 # abcdefg...ABCDEFG...
# punctuation
print(string.punctuation)                   # !@#$%^&*()_...


# test internal module1:
print(module1.variable1)
print(module1.variable2)

module1.func1()
module1.func2(100, 66.6)
module1.func3(7)
