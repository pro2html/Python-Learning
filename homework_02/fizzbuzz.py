import math

fizz = int(input('Please enter fizz '))
buzz = int(input('Please enter buzz '))
n    = int(input('Please enter N '))

for i in range(1, n + 1):
    if (not i % fizz and not i % buzz):
        print('FB', end=' ')

    elif (not i % fizz):
        print('F', end=' ')

    elif (not i % buzz):
        print('B', end=' ')

    else:
        print(str(i), end=' ')
        
print(end='\n')