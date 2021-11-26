# use 'break' to exit loop(while and for)
counter = 1
while counter < 11:
    if counter > 5:
        break
    print(counter)
    counter += 1


for i in range(100, 111):
    if i > 105:
        break
    print(i)


# use 'continue' to reject remain instructions
for i in range(200, 211):
    print(i)
    if i > 205:
        continue
    print('complex operation done!')
