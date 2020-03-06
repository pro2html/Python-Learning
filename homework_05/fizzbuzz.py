fizz = int(input('Please enter fizz '))
buzz = int(input('Please enter buzz '))
n    = int(input('Please enter N '))

def fizzbuzz(i):
    #variant 1
    #return 'FB' if (not i % fizz and not i % buzz) else 'F' if (not i % fizz) else 'B' if (not i % buzz) else str(i)
    
    #variant 2
    if (not i % fizz and not i % buzz):
        return 'FB'

    elif (not i % fizz):
        return 'F'

    elif (not i % buzz):
        return 'B'

    else:
        return str(i)

result = list(map(fizzbuzz, range(1, n + 1)))

print(result)

