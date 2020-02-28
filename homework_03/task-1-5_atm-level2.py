money_list = [10, 20, 50, 100, 200, 500, 1000]
user_money = 1
i          = 0
j          = 0
val_count  = 0


while user_money % 10:
    user_money = int(input('Введите число кратное 10 '))

print(user_money)

while user_money > 0:
    if(money_list[i] < 200):

        for j in range(0, 10):
            if(not user_money % money_list[i] and user_money // money_list[i] < 10):
                val_count = user_money // money_list[i]
                break

            elif (not (user_money - money_list[i]*j) % money_list[i + 1]):
                val_count = j

        user_money -= money_list[i] * val_count
        print('Купюр по ' + str(money_list[i]) + 'грн. - ' + str(val_count))
            
    else:
        val_count = user_money // money_list[i]
        user_money -= money_list[i] * val_count
        print('Купюр по ' + str(money_list[i]) + 'грн. - ' + str(val_count))

    val_count = 0
    i += 1


