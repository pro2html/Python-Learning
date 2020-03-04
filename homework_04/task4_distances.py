distances = [100, 50, 30, 40, 50, 80, 110, 200, 65, 10]
time      = [40, 30, 20, 10, 60, 20, 60, 80, 45, 3]
speed     = []

for i in range(1, 10):
    speed.append(round(distances[i]/time[i], 1))

mean = sum(speed)/len(speed)

print('\nСписок скоростей: ' + str(speed), end = '\n')

for i in speed:
    if i > mean:
        print(i, end = ', ')

print(end = '\n\n')