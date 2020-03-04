import random

numbers = [1,2,3,6,7,8,2,4,6,8,11,12,16,17]

cubic_number = [x**3 for x in numbers if x % 2 == 1]

print(cubic_number)