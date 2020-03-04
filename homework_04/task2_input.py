arr = []
arr.append(int(input('Введите число А: ')))
arr.append(int(input('Введите число B: ')))
arr.append(int(input('Введите число C: ')))

arr.sort()

for i in arr:
    print(i, end=' ')

print(end='\n')