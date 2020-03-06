numbers_list = [1, 4, 12, 2, 5, 7, 3, 2, 11, 13]

def simple_square(number):
    if(number == 1):
        return number

    for i in range(2, number + 1):
        if i != number and number % i == 0:
            return number
        elif i == number:
            return i ** 2

new_list = list(map(simple_square, numbers_list))
print(new_list)



