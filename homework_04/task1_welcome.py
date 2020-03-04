default_welcome = 'Welcome to California!'
countries_str  = 'USA, Ukraine, Russia, Italy, Spain'
countries_list   = []

countries_list = countries_str.split(', ')

for elem in countries_list:
    print(default_welcome[0:11] + elem + '!')