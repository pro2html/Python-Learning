import math
tea = True
cleanCup = True
hotWater = True

if(tea and cleanCup and hotWater):
    sugar = int(input("Введите количество ложек сахара "))

    if sugar:
        print("Чай с сахаром готов")
    else:
        print("Чай без сахара готов")


