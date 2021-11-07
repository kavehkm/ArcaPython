# echo everythin you want into console by print function
print('echo some text into console')

# get information from user by input function
name = input('whats yout name? ')

# print user's name into console with welcome message
print('welcome', name)


# define some variables
first_name = 'kaveh'
last_name = 'mehrbanian'
age = 26
average = 10.5
is_happy = True


# print variables with custom sep and end
# you must see result like this:
# kaveh***mehrbanian***26***10.5***True
#
#
print(first_name, last_name, age, average, is_happy, sep='***', end='\n\n')
