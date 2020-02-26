import math
a = int(input())

for i in range(1, math.ceil(math.sqrt(a)) + 1):
    if(not(a % i)):
        print(i)
        print(a // i)