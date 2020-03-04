import random

names = ['james', 'tom', 'symon', 'frodo', 'sergey']
last_names = ['romanov', 'cash', 'black', 'white', 'blue']
people_list = {}

for i in range(0,25):
    fullname = random.choice(names) + ' ' + random.choice(last_names)

    if(fullname in people_list):
        people_list[fullname] += 1
    else:
        people_list[fullname] = 1

print(str(people_list))