arr = []

for i in range(1, 10):
    arr.append(int(input('Введите число ')))

arr = [x*2 for x in arr]

print(arr)