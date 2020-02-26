import math
a = input()

for i in range(0, len(a)):
    print(a[i] + " - " + str(10 ** (len(a) - i - 1)))