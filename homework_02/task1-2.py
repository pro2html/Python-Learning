import math
a = int(input())

if(a % 2 and not a % 3 and not a % 5 and a % 10):
    print('suitable number')
else:
    print('wrong number')
