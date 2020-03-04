current      = 0
numbers_list = []

while (current < 1001):
    current = int(input('Введите число: '))
    numbers_list.append(current)

numbers_list.sort()


print('сумма всех чисел равна ' + str(sum(numbers_list)))
print('минимальное число ' + str(numbers_list[0]))
print('максимальное число ' + str(numbers_list[len(numbers_list) - 1]))
