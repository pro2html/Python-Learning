for i in range(1, 11):
    number = int(input())
    print(number if number % 2 != 0 and number % 3 == 0 else 'Не подходит')