number = int(input('Введите число: '))

for i in range(2, number + 1):
    if i != number and number % i == 0:
        print('Число не является простым')
        break
    elif i == number:
        print('Число является простым')
        break
