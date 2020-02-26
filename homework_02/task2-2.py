import math
apple = True
orange = False
potato = True
bag = True


purchases                = 'Яблоки в сумкке' if apple else 'Забыли яблоки'
fruits                   = orange or apple and 'Взяли фрукты' or 'Не взяли фрукты'
fruits_and_vegetables    = potato and (orange or apple) and bag and 'Учачно скупились' or 'Что-то забыли'


