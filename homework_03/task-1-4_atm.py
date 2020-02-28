money_list = [1000, 500, 200, 100, 50, 20, 10]
user_money = 1
i          = 0


while user_money % 10:
    user_money = int(input('Введите число кратное 10 '))

print(user_money)

while user_money > 0:
    n = user_money // money_list[i]
    if(not n):
        i += 1
        continue

    user_money -= n * money_list[i]

    print('Купюр по ' + str(money_list[i]) + 'грн. - ' + str(n))

    i += 1


