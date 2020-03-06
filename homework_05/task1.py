names_list     = ['Sara', 'Anton', 'Stas']
lastnames_list = ['Conor', 'Chonka', 'Bakanov']

def to_low(string):
    return string.lower()


def to_upper(string):
    return string.upper()

upper_str = list(map(to_upper, names_list))
print(upper_str)

lower_str = list(map(to_low, lastnames_list))
print(lower_str)